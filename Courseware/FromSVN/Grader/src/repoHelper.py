# FIXME: This file needs to be reworked!!!!!!!!!

"""
A RepoHelper can checkout repositories,
return the pathname where a repository is stored,
and return the usernames from a course.

Authors:  David Mutchler, David Lam, Mark Hays and their colleagues.
Version 1.1:  May, 2015.
"""
# FIXME: Above comment is no longer correct.

import os
import re
import subprocess


# NOTE: Change the GRADING_FOLDER as needed for your computer.
# 'C:/EclipseWorkspaces/csse120-grading/'
GRADING_FOLDER = '/Users/david/EclipseWorkspaces/grading/'
URL_FOR_SVN_REPOS = 'http://svn.csse.rose-hulman.edu/repos/'


# TODO: Move the SVN-specific stuff from the following class
#       to SVNHelper class.  Leave RepoHelper an abstract class.
class RepoHelper(object):
    """
    Abstract class, subclass must specify ???
    A RepoHelper can checkout repositories for a course,
    return the pathname where a repository is stored,
    and return the usernames from a course.
    """
    # TODO: Fix the above comment.

    def __init__(self, what_to_grade=None):
        self.what_to_grade = what_to_grade

    def project_name(self, session):
        """
        Returns the project name for the given session number.
        """
        # FIXME: This is not adequate, see comments elsewhere about it.
        session = int(session)  # To allow a string, e.g. '01' for 1
        return self.course.projects[session]

    def checkout_for_grading(self, what_to_grade, students,
                             force_checkout=False):
        """
        Checkouts the given project for all the given list of students.
        Returns three lists:
          -- students for which the checkout appears to have failed
          -- students skipped (because they were already checked out)
          -- all remaining students
        """
        # CONSIDER: Allow checking out things other than projects??
        failures, skips, successes = [], [], []
        for student in students:
            url = self.get_url(what_to_grade, student)
            folder = self.get_grading_folder(student)
            if not force_checkout and os.access(folder, os.F_OK):
                skips.append(student)
                continue

            result = self.checkout(url, folder)
            if result:
                successes.append(student)
            else:
                failures.append(student)

        return (failures, skips, successes)

    def get_url(self, what_to_grade, student):
        """
        Returns the URL for the given student's ThingToGrade.
        :type what_to_grade: ThingToGrade
        """
        repo = URL_FOR_SVN_REPOS + what_to_grade.course.students_repo \
            + '-' + student + '/' + what_to_grade.project_name
        return repo

    def get_grading_folder(self, student=None):
        """
        Returns the folder into which to checkout
        this RepoHelper's project (or the folder into which it was
        checked out, if student is not None).

        :rtype str
        """
        # FIXME:
        # This presumes a folder structure that others might not want.
        # But at least the structure is encapsulated in this function.
        folder = GRADING_FOLDER
        folder += self.what_to_grade.course.term + '/'
        folder += self.what_to_grade.project_name + '/'

        if student:
            folder += student + '/'

        return folder

    def get_usernames(self, groups=None):
        """
        The argument, if present, is either a section number
        or a sequence of group names.  Returns a list of usernames
        for that section or for that sequence of group names.
        """
        if not groups:
            sections = self.course.sections
        else:
            # TODO: Is there a better way to tell whether
            #       groups is a sequence?
            try:
                len(groups)
                # FIXME: Deal with this case.  See commented-out code.
            except:
                sections = [groups]

        # FIXME: Really should get this information from the
        #        course web site.  See commented-out code.
        usernames = []
        for section in sections:
            file = open('usernames-' + str(section) + '.txt', 'r')
            for username in file.readlines():
                usernames.append(username.strip())
        return usernames

#     url_prefix = roster_folder + COURSE + '-' + TERM + '-'
#     for group in groups:
#         url = url_prefix + group + '.txt'
#         print(url)
#         usernames_as_byte_array = urllib.request.urlopen(url).read()
#         usernames_in_group = usernames_as_byte_array.decode().split()
#         usernames.extend(usernames_in_group)
#
#     return usernames

    def checkout(self, url, folder):
        """
        Checks out the given URL into the given folder.
        Returns True if the checkout succeeded, else False.
        """
        # FIXME: You need to make Tortoise learn your password somehow.
        #    Otherwise, use something like:
        #      os.system('svn checkout ' + url + ' ' + folder
        #            + ' --username mutchler --password XXX')
        #    But note that the latter is a security hazard
        #    (see me for details).
        try:
            command = ('svn checkout ' + url + ' ' + folder
                        + ' --username mutchler --password Lego2222')
            print(command)
#             result = subprocess.call(command, stderr=subprocess.DEVNULL)
            result = os.system(command)
            return (True if result == 0 else False)
        except:
            return False

    def get_number_of_commits(self, student):
        folder = self.get_grading_folder(student)
        command = ('svn log -q ' + folder
                   + ' --username mutchler --password Lego2222')
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        # FIXME: This assumes  svn log  works the way that it does for my Mac
        output = result.stdout.split(b'\n')
        return (len(output) - 2) // 2

    def fix_all_for_eclipse(self, project, students):
        """
        For each of the given students, renames the project to be the
        student's username.  This allows all the projects to exist in a
        single Eclipse workspace.
        Returns a list of students for whom this failed for any reason.
        """
        failures = []
        for student in students:
            try:
                folder = self.get_grading_folder(student, project)
                result = self.fix_for_eclipse(folder, project, student)
                if not result:
                    failures.append(student)
            except:
                failures.append(student)

        return failures

    def fix_for_eclipse(self, folder, project, student):
        """
        Modifies the  .project  file in the given folder to rename
        the project from its name to the given student (username).
        This allows Eclipse to import  multiple students' projects
        for the same assignment (all of which share the same project
        name before running this function).
        Returns  True  if this action succeeded, else returns  False.
        """
        # FIXME: The following is brittle and WILL BREAK if
        #        Eclipse changes its project filenames.
        filename = folder + '/.project'
        try:
            with open(filename, 'r') as file:
                file_contents = file.read()

            lines = file_contents.split('\n')
            with open(filename, 'w') as file:
                for line in lines:
                    print(re.sub(project, student, line), file=file)
        except:
            # FIXME: Figure out whether this detects failures correctly.
            print('Could not open the file:')
            print('   ', filename)
            ('Fix and try again.\n')
            return False

        return True


import urllib.request
import time


def see_if_changed(url, old):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(html)

    if html != old:
        for k in range(100):
            print('New')


def exists(start):
    html = []
    for k in range(10):
        url_base = 'http://docquery.fec.gov/cgi-bin/fecimg?_20160620'
        url = url_base + str(start + k) + '+0'
        with urllib.request.urlopen(url) as response:
            html = response.read()
            if b'ERROR' in html:
                continue
#                 print(start, k, html)
#                 break
            else:
                return (start, k, html)
#             print(html)
#             html.append(response.read())
#     for k in range(len(html[0])):
#         if html[0][k] != html[1][k]:
#             print(k, html[0][k], html[1][k])
#     print(html[0][700:750])
#     print(html[1][700:750])
#     return
#     for k in range(10):
#         print(k)
#         if html[k] != html[k + 1]:
#             print(html[k + 1])
#             return


def main():
    newest = 9019070413
#     exists(9019068796)
    while True:
        result = exists(newest)
        if result:
            break
    print(result)
    number = result[0] + result[1]
    folder = str(number)[-3:]
    date = '20160620'
    print('docquery.fec.gov/pdf/{}/{}{}/{}{}.pdf'.format(folder,
                                                         date, number, date, number))
#     while True:
#         old = b'\r\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\r\n        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\r\n\r\n<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="en-US">\r\n<head>\r\n\t<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />\r\n\t<meta http-equiv="content-type" content="text/html; charset=UTF-8" />\r\n\r\n\t<title>Committee/Candidate Details</title>\r\n\t\r\n\t<link rel="stylesheet" href="/stylesheets/fec_sitestyles.css" type="text/css" />\r\n\t<link rel="stylesheet" href="/stylesheets/fec_apps.css" type="text/css" />\r\n\t<link rel="stylesheet" href="/stylesheets/fec_forms.css" type="text/css" />\r\n\t<link rel="stylesheet" href="/stylesheets/fec_table.css" type="text/css" />\r\n\t<link rel="stylesheet" href="/stylesheets/fec_export.css" type="text/css" />\r\n\t<link rel="stylesheet" href="/stylesheets/disclosure.css" type="text/css" />\r\n\r\n\t<link rel="stylesheet" href="/stylesheets/jquery/jquery.ui.all.css" type="text/css" />\r\n\t<link rel="stylesheet" href="/stylesheets/jquery/jquery.ui.theme.css" type="text/css" />\r\n\t<link rel="stylesheet" href="/stylesheets/jquery/jquery.ui.tabs.css" type="text/css" />\r\n\t<link rel="stylesheet" href="/stylesheets/jquery/jquery.ui.core.css" type="text/css" />\r\n\t<link rel="stylesheet" href="loc_css/imagesearch.css" type="text/css" />\r\n\t\r\n\t\r\n\t    \r\n\t\r\n<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\r\n\r\n\r\n\r\n<html>\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">\r\n<title></title>\r\n</head>\r\n<body>\r\n<script src="/app_javascript/jquery/jquery-1.10.2.min.js"></script>\n<script src="/app_javascript/jquery/jquery-migrate-1.2.1.min.js"></script>\n\n\r\n</body>\r\n</html> \r\n\t\r\n\t<script type="text/javascript" src="/app_javascript/jquery/jquery.ui.core.js"></script>\r\n\t<script type="text/javascript" src="/app_javascript/jquery/jquery.ui.widget.js"></script>\r\n\t<script type="text/javascript" src="/app_javascript/jquery/jquery.ui.tabs.js"></script>\r\n\t<script type="text/javascript" src="/app_javascript/jsapi.js"></script>\t\r\n\t<script type="text/javascript">\r\n\r\n\t\t\r\n\t\tfunction getParameterByName(name) {\r\n\t\t\tname = name.replace(/[\\[]/, "\\\\[").replace(/[\\]]/, "\\\\]");\r\n\t\t\tvar regex = new RegExp("[\\\\?&]" + name + "=([^&#]*)"),\r\n\t\t\t\tresults = regex.exec(location.search);\r\n\t\t\treturn results === null ? "null" : decodeURIComponent(results[1].replace(/\\+/g, " "));\r\n\t\t}\r\n\t\t$(function() {\r\n\t\t\tvar pc = \'\';\r\n\t\t\tif($("#progressControl").length == 0) {\r\n\t\t\t\tpc = \'<div id="progressControl" class="progressControl"><img src="/images/app_img/progress.gif" alt="Loading Icon"/></div>\';\r\n\t\t\t\t$("#tabs").append(pc);\t\r\n\t\t\t}\r\n\t\t<!--\tvar tabIndex = "1";-->\r\n\t\t\r\n//alert(\'tabIndexQryString:\'+tabIndexQryString);\r\n\t\t\tvar tab = sessionStorage.getItem(\'tabIndex\');\r\n\t\t\tvar tabIndex = sessionStorage.getItem(\'tabIndexSession\');\r\n\t\t\tif(sessionStorage.getItem(\'tabIndexSession\') != null){\r\n//alert(\'In the if condition\');\t\t\t\t\r\n\t\t\t\ttabIndex = sessionStorage.getItem(\'tabIndexSession\');\r\n\t\t\t}\r\n\t\t\telse {\r\n//alert(\'In the else condition\');\r\n\t\t\t\tvar tabIndexQryString = getParameterByName(\'tabIndex\');\r\n\t\t\t\tif(tabIndexQryString != \'null\' ){\r\n\t\t\t\t\ttabIndex = tabIndexQryString;\r\n\t\t\t\t\ttabIndexSession = tabIndexQryString;\r\n\t\t\t\t} else{\r\n\t\t\t\t\ttabIndex = sessionStorage.getItem(\'tabIndex\');\r\n\t\t\t\t\tsessionStorage.setItem(\'tabIndexSession\',tabIndex);\r\n\t\t\t\t}\r\n\t\t\t}\r\n\t\t\t\r\n\t\t\t$("#tabs").bind("tabsselect", function(event, ui) {\r\n\t\t\t\tif($("#progressControl").length == 0) {\r\n\t\t\t\t\tvar pc = \'<div id="progressControl" class="progressControl"><img src="/images/app_img/progress.gif" alt="Loading Icon"/></div>\';\r\n\t\t\t\t\t$("#tabs").append(pc);\r\n\t\t\t\t}\r\n\t\t\t\twindow.location.hash = ui.index+1;\r\n\t\t  \t});\r\n\t\t\tif(window.location.hash != null && window.location.hash != "") {\r\n\t\t\t\ttabIndex = window.location.hash.substring(1, 2);\r\n\t\t\t}\r\n\t\t\tvar $selectedTab = $( "#tabs" ).tabs({\r\n\t\t\t\tajaxOptions: {\r\n\t\t\t\t\terror: function( xhr, status, index, anchor ) {\r\n\t\t\t\t\t\t$( anchor.hash ).html(\r\n\t\t\t\t\t\t\t"Loading...");\r\n\t\t\t\t\t}\r\n\t\t\t\t}\r\n\t\t\t});\r\n\t\t\t\r\n\t\t    //$selectedTab.tabs(\'option\', \'selected\', tabIndex);\r\n\t\t\t\r\n            if (tabIndex > 1)\r\n                    $selectedTab.tabs(\'option\', \'active\', tabIndex - 1);\r\n            else\r\n                    $selectedTab.tabs(\'option\', \'active\', 0);\t\t\t\r\n\t\t});\r\n\t\tgoogle.load("visualization", "1", {packages:["corechart"]});\r\n\t\t\r\n/* \t\tfunction assignTabIndex(){\r\n\t\t\talert(\'tabIndexSession: \'+sessionStorage.getItem(\'tabIndexSession\'));\r\n//\t\t\talert(\'selected tab value:\'+document.getElementById(\'selectedTabIndex\').value);\r\n\t\t\t\r\n\t\t\tvar highlightKeyOld = $("#myVar").val();\r\n\t\t\tdocument.getElementById(\'selectedTabIndex\').value="1";\r\n//\t\t\talert(\'selected tab value:\'+document.getElementById(\'selectedTabIndex\').value);\r\n\t\t}\r\n */\t</script>\r\n</head>\r\n<body>\r\n\r\n    \r\n\r\n<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\r\n\r\n\r\n\r\n<html>\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">\r\n<title></title>\r\n</head>\r\n<body>\r\n<!-- Banner -->\n<div id="banner">\n\t\t<div class="title">Try out <a href="https://beta.fec.gov/">betaFEC</a></div>\n\t\t<div class="subtitle">With new tools for viewing campaign finance data.</div>\t\n</div>\n<div id="fec_logoArea">\n\t<a href="/"><img src="/images/fec_corner_logo.gif" alt="Federal Election Commission, United States of America (logo). Link to FEC Home Page" width="159" height="221" border="0"></a>\n</div>\n\n<div id="fec_nameArea">\n\t<img src="/images/fec_name.gif" alt="Federal Election Commission" width="357" height="66" border="0">\n</div>\n\n<div id="topNav">\n\t<ul>\n\t\t<li /><a href="/about.shtml">About the FEC</a>\n\t\t<li /><a href="/press/press.shtml">Press Office</a>\n\t\t<li /><a href="/ans/answers.shtml">Quick Answers</a>\n\t\t<li /><a href="/pages/contact.shtml">Contact Us</a>\n\t\t<li /><a href="/sitemap.shtml">Site Map</a>\n\t</ul>\n</div>\n\n<div id="fec_mainToolbar">\n\t<!-- top navigation cascading menu will appear in this area -->\n\t<div class="fec_searchForm">\n\t<form action="http://search04.fec.gov/vivisimo/cgi-bin/query-meta"><font color="white"><strong>FEC Search</strong></font>\n\t\t\t<input name="query" />\n\t\t\t<input type="hidden" name="v:project" value="fec_search_02_prj" />\n\t\t\t<span class="fec_submitBtn">\n\t\t\t\t\t<input type="image" src="/images/btn_search.png" alt="Search button" id="fec_submitBtn">\n\t\t\t</span>\n\t</form> \n\t</div>\n</div>\n<div id="fec_skipNav">\n\t<a href="#content">Skip Navigation</a>\n</div>\n\r\n</body>\r\n</html> \r\n<!-- \r\n\r\n-->\r\n<div id="breadcrumbs">\r\n<a href="/index.shtml">HOME</a>\r\n / <a href="/pindex.shtml">CAMPAIGN FINANCE DISCLOSURE PORTAL</a>\r\n / <a href="/finance/disclosure/candcmte_info.shtml?tabIndex=1">CANDIDATE AND COMMITTEE VIEWER</a>\r\n / <span class="breadcrumbs_curPage">\r\n\tCOMMITTEE DETAILS\r\n</span>\r\n</div>\r\n\r\n    \r\n\r\n<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\r\n\r\n\r\n\r\n<html>\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">\r\n<title></title>\r\n</head>\r\n<body>\r\n<link rel="stylesheet" href="/stylesheets/p_left_menu.css" type="text/css" />\n<script type="text/javascript" src="/app_javascript/leftmenu.js"></script>\n<div>\n\t<div class="left_menu_right_border"></div>\n\t<div class="left_menu_bottom_border"></div>\n</div>\n<div class="leftsection">\n<ul id="leftmenu" class="collapsible">\n\t<li id="datacatalog">\n\t\t<a class="head" href="#"><img border="0" style="vertical-align:middle" alt="Data Catalog" src="/images/menus/leftmenu/database.png"></img>&nbsp;Data Catalog</a>\n\t\t<ul class="acitem oneleftpadding">\n\t\t\t<li><a class="menu_item" href="/data/DataCatalog.do?format=html" id="dc">&nbsp;Data Catalog Home</a></li>\n\t\t\t<li><a class="menu_item" href="/data/AdminFine.do?format=html" id="af"><!-- <img border="0" style="vertical-align:middle" src="images/menus/leftmenu/arrow.png"></img>-->&nbsp;Administrative Fines</a></li>\n\t\t\t<li><a class="menu_item" href="/data/LobbyistBundle.do?format=html" id="lb"><!-- <img border="0" style="vertical-align:middle" src="images/menus/leftmenu/arrow.png"></img>-->&nbsp;Bundled Contributions</a></li>\n\t\t\t<li><a class="menu_item" href="/data/CampaignAndCommitteeSummary.do?format=html" id="ccs"><!-- <img border="0" style="vertical-align:middle" src="images/menus/leftmenu/arrow.png"></img>-->&nbsp;Committee Report <br>&nbsp;Summary</a></li>\n\t\t\t<li><a class="menu_item" href="/data/CandidateDisbursement.do?format=html" id="cd"><!-- <img border="0" style="vertical-align:middle" src="images/menus/leftmenu/arrow.png"></img>-->&nbsp;Candidate <br>&nbsp;Disbursements</a></li>\n\t\t\t<li><a class="menu_item" href="/data/CandidateSummary.do?format=html" id="cds"><!-- <img border="0" style="vertical-align:middle" src="images/menus/leftmenu/arrow.png"></img>-->&nbsp;Candidate Summary</a></li>\n\t\t\t<li><a class="menu_item" href="/data/CommitteeSummary.do?format=html" id="cms"><!-- <img border="0" style="vertical-align:middle" src="images/menus/leftmenu/arrow.png"></img>-->&nbsp;Committee Summary</a></li>\n\t\t\t<li><a class="menu_item" href="/data/CommunicationCosts.do?format=html" id="cc">&nbsp;Communication Costs</a></li>\n\t\t\t<li><a class="menu_item" href="/data/EnhancedElectioneeringCommunications.do?format=html" id="ec">&nbsp;Electioneering<br>&nbsp;Communications</a></li> \n\t\t\t<li><a class="menu_item" href="/data/IndependentExpenditure.do?format=html" id="ie"><!-- <img border="0" style="vertical-align:middle" src="images/menus/leftmenu/arrow.png"></img>-->&nbsp;Independent<br>&nbsp;Expenditures</a></li>\n\t\t\t<li><a class="menu_item" href="/data/Leadership.do?format=html" id="ls"><!-- <img border="0" style="vertical-align:middle" src="images/menus/leftmenu/arrow.png"></img>-->&nbsp;Leadership PACs <br>&nbsp;and Sponsors</a></li>\n\t\t\t<li><a class="menu_item" href="/data/Lobbyist.do?format=html" id="lo"><!-- <img border="0" style="vertical-align:middle" src="images/menus/leftmenu/arrow.png"></img>-->&nbsp;Lobbyist/Registrant</a></li>\n\t\t\t<li><a class="menu_item" href="/data/Form1Filer.do?format=html" id="f1f">&nbsp;New Committee<br/>&nbsp;Registrations</a></li>\n\t\t\t<li><a class="menu_item" href="/data/Form2Filer.do?format=html" id="f2f">&nbsp;New Statements<br/>&nbsp;of Candidacy</a></li>\t\t\n\t\t</ul> \n\t</li>\n\t<li id="maps">\n\t\t<a class="head" href="#">\n\t\t<img border="0" style="vertical-align:middle" alt="Maps" src="/images/menus/leftmenu/usa_map.png"></img>&nbsp;Maps</a>\n\t\t<ul class="acitem oneleftpadding">\n\t\t\t<li><a class="menu_item" href="/disclosurep/pnational.do" id="p"><!-- <img border="0" style="vertical-align:middle" src="images/menus/leftmenu/arrow.png"></img>--><!-- <img border="0" style="vertical-align:middle" src="images/menus/leftmenu/p.png"></img> -->&nbsp;Presidential</a></li>\n\t\t\t<li><a class="menu_item" href="/disclosurehs/hsnational.do" id="hs"><!-- <img border="0" style="vertical-align:middle" src="images/menus/\tleftmenu/arrow.png"></img>--><!-- <img border="0" style="vertical-align:middle" src="images/menus/leftmenu/hs.png"></img>-->&nbsp;House &amp; Senate</a></li>\n\t\t\t<li><a class="menu_item" href="/disclosureie/ienational.do" id="hien">&nbsp;House Independent<br>&nbsp;Expenditures</a></li>\n\t\t\t<li><a class="menu_item" href="/disclosureie/ienational.do?candOffice=S" id="sien">&nbsp;Senate Independent<br>&nbsp;Expenditures</a></li>\n\t\t\t<!--<li id="os"><a class="sub_menu_head menu_item" href="javascript:void(0);">&nbsp;Outside Spending</a>\n\t\t\t\t<ul class="acitem oneleftpadding">\n\t\t\t\t\t<li><a class="menu_item" href="/disclosureie/ienational.do" id="ien">&nbsp;House Independent<br>&nbsp;Expenditures</a></li>\n\t\t\t\t</ul> \t\t\t\n\t\t\t</li>-->\n\t\t</ul> \n\t</li>\n\t<li id="charts">\n\t\t<a class="head" href="#">\n\t\t<img border="0" style="vertical-align:middle" alt="Charts" src="/images/menus/leftmenu/charts.png"></img>&nbsp;Charts</a>\n\t\t<ul class="acitem oneleftpadding">\n\t\t\t<li><a class="menu_item" href="/disclosure/pacSummary.do" id="pac"><!-- <img border="0" style="vertical-align:middle" src="images/menus/leftmenu/arrow.png"></img>-->&nbsp;PACs</a></li>\n\t\t\t<li><a class="menu_item" href="/disclosure/partySummary.do" id="pty"><!-- <img border="0" style="vertical-align:middle" src="images/menus/leftmenu/arrow.png"></img>-->&nbsp;National Parties</a></li>\n\t\t</ul> \n\t</li>\n\t<li id="search">\n\t\t<a class="head" href="#">\n\t\t<img border="0" style="vertical-align:middle" alt="Search" src="/images/menus/leftmenu/search_thumb.png"></img>&nbsp;Search</a>\n\t\t<ul class="acitem oneleftpadding">\n\t\t\t<li><a class="menu_item" href="/finance/disclosure/candcmte_info.shtml" id="ccv">&nbsp;Candidate & Committee <br>&nbsp;Viewer</a></li>\n            <li><a class="menu_item" href="/data/index.jsp" id="pac">&nbsp;Data Catalog</a></li>\n\t\t\t\n\t\t\t\n\t\t\t<li><a class="menu_item" href="http://efilingapps.fec.gov/rss/display?input" id="rss">&nbsp;Electronic Filing RSS Feed</a></li>\n            <li><a class="menu_item" href="http://www.fec.gov/finance/disclosure/ie_reports.shtml" id="ie">&nbsp;Independent<br>&nbsp;Expenditure Search</a></li>\n\t\t\t\n\t\t\t<li><a class="menu_item" href="http://www.fec.gov/finance/disclosure/norindsea.shtml" id="ie">&nbsp;Individual<br>&nbsp;Contribution Search</a></li>\n\t\t\t\n\t\t</ul> \n\t</li>\n\t<li id="download">\n\t\t<a class="head" href="#">\n\t\t<img border="0" style="vertical-align:middle;" alt="Download" src="/images/menus/leftmenu/download_thumb.png"></img>&nbsp;Download</a>\n\t\t<ul class="acitem oneleftpadding">\n\t\t\t<li><a class="menu_item" href="/data/index.jsp" id="dc">&nbsp;Data Catalog</a></li>\n\t\t\t<li><a class="menu_item" target="ftp_download" href="http://www.fec.gov/finance/disclosure/ftp_download.shtml" id="ftp">&nbsp;Larger Data Sets</a></li>\n\t\t\t<li><a class="menu_item" target="electioneering" href="http://www.fec.gov/finance/disclosure/electioneering.shtml" id="ec">&nbsp;Electioneering<br>&nbsp;Communications</a></li>\n\t\t\t<li><a class="menu_item" target="2012matching" href="http://www.fec.gov/finance/2012matching/2012matching.shtml" id="pm">&nbsp;Presidential Matching<br>&nbsp;Funds Submissions</a></li>\n\t\t\t<li><a class="menu_item" target="ftpdet" href="http://www.fec.gov/finance/disclosure/ftpdet.shtml" id="df">&nbsp;Contribution Files</a></li>\n\t\t\t<li><a class="menu_item" target="ftpsum" href="http://www.fec.gov/finance/disclosure/ftpsum.shtml" id="sf">&nbsp;Campaign Summaries</a></li>\n\t\t\t<li><a class="menu_item" target="ftpefile" href="http://www.fec.gov/finance/disclosure/ftpefile.shtml" id="ef">&nbsp;Electronically Filed<br>&nbsp;Reports (.FEC files)</a></li>\n\t\t</ul> \n\t</li>\n</ul>\n</div>\n\r\n</body>\r\n</html> \r\n<!-- Add menu tabs here -->\r\n<div id="app_header_1"><a name="content"></a>\r\n\t<h1><!--2016&nbsp;-->\r\n\tDetails for Committee ID\r\n\t: C00605568</h1>\r\n</div>\r\n\r\n<div id="app_main_content_tabs"> \r\n\t<div id="tabs">\r\n\t\t<ul>\r\n\t\t\t<li><a href="CommitteeDetailCurrentSummary.do?tabIndex=1&candidateCommitteeId=C00605568&electionYr=2016" >Two-Year Summary</a></li>\r\n\t\t\t<li><a href="CommitteeDetailCurrentReportList.do?tabIndex=2&candidateCommitteeId=C00605568&electionYr=2016" >Report Summaries</a></li>\t\t\t\r\n\t\t\t<li><a href="CommitteeDetailFilings.do?tabIndex=3&candidateCommitteeId=C00605568&electionYr=2016" >Filings</a></li>\r\n\t\t</ul>\r\n\t</div>\r\n</div>\r\n\r\n\r\n    \r\n\r\n<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\r\n\r\n\r\n\r\n<html>\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">\r\n<title></title>\r\n</head>\r\n<body>\r\n<div id="fec_footer">\n\n\t<div class="fec_footerLinks">\n\t\n\t\t<!-- Verdana Bold 10/12 gray, hover underline -->\n\t\n\t\t<ul>\n\t\t<nofollow>\n\t\t<li><a href="/general/whatsnew.shtml" title="What&#0146;s New on FEC.gov" accesskey="n">What&#0146;s New</a>\n\t\t<li><a href="/general/library.shtml" title="FEC Publications and Forms">Library</a>\n<li><a href="/press/foia.shtml" title="Freedom of Information Act">FOIA</a>\n\t\t<li><a href="http://www.usa.gov/" title="Official information and services from the U.S. government">USA.gov</a>\n\t\t<li><a href="/privacy.shtml" title="FEC.gov Privacy Policy">Privacy</a>\n\t\t<li><a href="/links_files/Links.shtml" title="Links to Election-Related Web Sites">Links</a>\n\t\t<li><a href="/elecfil/electron.shtml" title="Electronic Filing">eFiling</a>\n\t\t<li><a href="/fecig/fecig.shtml" title="The National Mail Voter Registration Form">Inspector General</a>\n\t\t<li><a href="/eeo/NoFear.shtml" title="No Fear Act">No Fear Act</a>\n        <li><a href="/info/fecmaill.shtml"><img src="/images/envelope.jpg" alt=" " width="15" height="10" border="0"></a>\t<a href="/info/fecmaill.shtml">Subscribe</a>\t        \n\t\t</nofollow>\n\t\t</ul>\n  </div>\n\n\t<div class="fec_footerInfo">\n\t\n\t\t<!-- Verdana 9/11 -->\n\t\t<!-- link: bold, red, hover underline -->\n\t\t\n\t  <p>Federal Election Commission, 999 E Street, NW, \n\t\tWashington, DC 20463 (800) 424-9530 \n\t\tIn Washington (202) 694-1000<br>   \n\t\tFor the hearing impaired, TTY (202) 219-3336\n\t\tSend comments and suggestions about this site to the <a href="/about/offices/CIO/webmanager/webmanager.shtml">web manager</a>.</p>\n\t\n\t</div>\n\t\n  <script type="text/javascript"> \n    var _gaq = _gaq || []; \n    _gaq.push([\'_setAccount\', \'UA-16134356-1\']); \n    _gaq.push([\'_trackPageview\']); \n    (function() { \n      var ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true; \n      ga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\'; \n      var s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s); \n    })(); \n  </script> \n\n<!-- Google Website Optimizer tracking script -->\n <script type="text/javascript"> \n  var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");\n  document.write(unescape("%3Cscript src=\'" + gaJsHost + "google-analytics.com/ga.js\' type=\'text/javascript\'%3E%3C/script%3E"));\n </script>\n <script type="text/javascript"> \n  try{\n   var gwoTracker = _gat._getTracker("UA-16134356-1"); \n   gwoTracker._trackPageview(); \n  } catch(err) {}\n </script>\n\n\n</div>\n\r\n</body>\r\n</html> \r\n</body>\r\n</html>'
#         see_if_changed('http://www.fec.gov/fecviewer/CandidateCommitteeDetail.do?candidateCommitteeId=C00605568&tabIndex=1', old)
#         time.sleep(0.1)
#         break
#     return
#     csse120 = course.Course('csse', '120', '201640', ['01'])
#     what_to_grade = grader.ThingToGrade(csse120, 'Session10_MoreImplementingClasses')
#     rh = RepoHelper(what_to_grade)
#     a, b, c = rh.checkout_for_grading(what_to_grade, csse120.get_usernames())
#     print(a)
#     print(b)
#     print(c)


if __name__ == '__main__':
    main()


# ----------------------------------------------------------------------
# NOTE: The following code assumes that you have installed Tortoise SVN
#       and put command-line tools (e.g.   svn   ) in your system path.
# ----------------------------------------------------------------------
class SVNRepoHelper(RepoHelper):
    """
    An Subversion (SVN) implementation, hosted by CSSE,
    of the RepoHelper abstract class.
    """
    # TODO: Pull SVN-specific stuff from RepoHelper (above) to here.


class StandardRepoHelper(SVNRepoHelper):
    """ The default class to use as RepoHelper is a SVNRepoHelper. """


# ----------------------------------------------------------------------
# NOTE: The following code is not currently used.
# ----------------------------------------------------------------------
#
#
# class Student(object):
#     def __init__(self, username, name, campus_mail, major, class_, year,
#                  advisor, email):
#         self.username = username
#
#
# # class Checker_Outer(object):
# #     default_course = 'csse120'
# #
# #     def __init__(self, course=Checker_Outer.default_course, term=None):
# #         self.course = course
# #         # TODO: Determine the term from today's date.
# #         self.term = 201510
# #         # TODO: Determine the sections from Schedule Lookup Page.
# #         self.sections = ['01', '02', '03', '04']
# #
# #         self.url_for_course_lookup = URL_FOR_SCHEDULE_LOOKUP
# #
# #     def enrolled_students(self, section=None):
# #         """
# #         Returns a list of all the Student  (u that are members of the given sequence
# #         of groups.  The usernames must be stored in text files that
# #         are in the appropriate place.
# #         """
# #         students = []
# #         url_prefix = roster_folder + COURSE + '-' + TERM + '-'
# #     for group in groups:
# #         url = url_prefix + group + '.txt'
# #         usernames_as_byte_array = urllib.request.urlopen(url).read()
# #         usernames_in_group = usernames_as_byte_array.decode().split()
# #         usernames.extend(usernames_in_group)
# #
# #     return usernames
#
#
# # def main():
# #     start(0)
# #
# #
# # def start(project_number):
# #     project = PROJECTS[project_number]
# #     students = get_usernames_from_rosters()
# #
# #     failures1 = checkout_all(project, students)
# #     failures2 = fix_all_for_eclipse(project, students)
# #     print('Failed checkout:', failures1)
# #     print('Failed fix-for-Eclipse:', failures2)
# #
# #     remove_extra(project, students)
#
#
# #     checkout_solution(project)
# #     folder = get_grading_folder(SOLUTION_USERNAME, project)
# #     fix_for_eclipse(folder, project + SOLUTION_SUFFIX,
# #                     SOLUTION_USERNAME)
#
#
#
#
#
#
#
# def checkout_solution(project_to_grade, solution_name=None):
#     """
#     Checkouts the solution for the given project.
#     Puts it in the same place as the student solutions are placed.
#     Returns True if succeeded, else False.
#     """
#
#     url = get_solution_url(project_to_grade)
#     folder = get_grading_folder(SOLUTION_USERNAME, project_to_grade)
#     if os.access(folder, os.F_OK):
#         print('WARNING: SKIPPING', folder, 'because it already exists')
#         return False
#     success_or_failure = checkout(url, folder)
#     return success_or_failure
#
#
#
# def get_solution_url(project_to_grade):
#     """ Returns the URL for the solution for the given project. """
#     repo = COURSE_REPO_NAME + '/' + ECLIPSE_PROJECTS + '/' + TERM
#     solution = project_to_grade + SOLUTION_SUFFIX
#     return URL_FOR_SVN_REPOS + repo + '/' + solution
#
#
#
#
#
#
#
#
# # Functions below are NOT correct.
#
# def remove_extra(project_to_grade, students):
#     """
#     Removes all unnecessary information from the projects:
#       -- All SVN information
#       -- All .docx and .pdf files
#     """
#     for student in students:
#         folder = get_grading_folder(student, project_to_grade)
#         remove_extra_in_folder(folder)
#
#
# def remove_extra_in_folder(folder):
#     """
#     At the TOP level of the given folder,
#     as well as in the   src   subfolder (if it exists),
#     removes any of the following that exist:
#       *.docx, *.pdf, *.gif
#     """
#     # FIXME: THIS IS A DANGEROUS FUNCTION.
#     #        If the folder is somehow not what is intended,
#     #        LOTS of files can be IRREVOCABLY DELETED.
#
#     # Temporary attempt at safety:
#     try:
#         assert(folder.startswith(GRADING_FOLDER))
#     except:
#         print('ERROR ERROR ERROR in remove_extra_in_folder')
#         raise Exception('Error in remove_extra_in_folder')
#
#     # Here is the dangerous part:
#     for file in os.listdir(folder):
#         if (file == '.svn'):
#             pass  # shutil.rmtree(folder + '/.svn')
#         if fnmatch.fnmatch(file, '*.pdf'):
#             os.remove(folder + '/' + file)
#         if fnmatch.fnmatch(file, '*.docx'):
#             os.remove(folder + '/' + file)
#
#     for file in os.listdir(folder + '/src'):
#         if fnmatch.fnmatch(file, '*.gif'):
#             os.remove(folder + '/src/' + file)
#
