# -*- coding: utf-8 -*-
{
    "name": "All-In-One Lists Reminders",
    "version": "11.0.1.0.4",
    "category": "Extra Tools",
    "author": "Odoo Tools",
    "website": "https://odootools.com/apps/11.0/all-in-one-lists-reminders-3",
    "license": "Other proprietary",
    "application": True,
    "installable": True,
    "auto_install": False,
    "depends": [
        "mail"
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/total_notify.xml",
        "data/mail_template.xml",
        "data/cron.xml"
    ],
    "qweb": [
        
    ],
    "js": [
        
    ],
    "demo": [
        
    ],
    "external_dependencies": {
        "python": [
                "xlsxwriter"
        ]
},
    "summary": "The tool to prepare and regularly send topical, filtered, all-in-one lists of any Odoo documents",
    "description": """
    Many users prefer simple lists to Odoo dynamic interfaces. Sometimes it is truly comfortable to open a set of documents and process them one by one without extra clicks. It is even better if the system prepares such a list for you regularly. Besides external partners usually do not have an access to objects, while certain statistics should be available and carefully shared. For such situations this tool serves. It let you configure <strong>automatic</strong> reminders for <strong>any Odoo document type</strong> in a form of lists, where each record will satisfy <strong>criteria you have chosen</strong>, will suit <strong>pre-defined time frames</strong>, and will contain only the data you would like to share.

    The module features are significantly expanded starting from the version 11. In case you migrate data from a lesser version, the reminders should be prepared from scratch
    The tool works for any Odoo documents. Look at the section <a href="#use-cases">Use cases</a>
    <strong>Any partner</strong> might be one of reminder recipients: internal or portal users, customers, suppliers, and even Odoo mail channels
    Lists' appearance is configurable and let you select columns to show. Look at the section <a href="#lists-view">Reminder view</a>
    Optionally attach an <strong>Excel (xlsx)</strong> table with the same list of documents
    Select topical documents based on relative periods: last or next days, weeks, months, years. Look at the section <a href="#periods">Periods</a>
    Apply any sort of filters to include only required documents. Look at the section <a href="#filtering">Filtering</a>
    Send lists at any moment: everyday, each last Friday of a month, on a definite date of the year, and so on. Look at the section <a href="#recurrence">Recurrence</a>
    Grant rights to configure reminders for any user. Look at the section <a href="#user-rights">User Rights</a
    # <a name='lists-view'></a> Reminder view
    Reminders' and attached tables' appearance is configurable, and let you select only essential and valuable data:
<ul>
<li>The tool allows choosing an unlimited number of columns for this document. It might be any field of a target model of the following types: char, text, html, integer, float, selection, boolean, date, datetime and relations to other documents (many2one, one2many, many2many). The set includes even computed fields</li>
<li>For relational fields you might choose the second level precision. For example, you might show a phone of a customer for a sales orders' reminder or tags' colors for tasks</li>
<li>It is possible to adapt column names. By default a field description is stated (on the language of this reminder), but users are allowed to change them</li>
<li>Optionally attach an xlsx table for reminders. It would have the same columns as a reminder itself. It is also possible to exclude a list from email and leave only an xlsx table</li>
<li>Include or exclude links to Odoo objects. References are great in case of internal reminders, but they are harmful in case of external ones</li>
<li>Introduce any greeting text for a notification</li>
<li>Choose reminders' language</li>
<li>Do <strong>not</strong> change email template manually. It will break all styles. Look at the Configuration tab</li>
</ul>
    # <a name='periods'></a>Periods
    <div class="alert alert-warning">
<span style="font-size:18px">
    <i class="fa fa-book"></i> Take into account that if a related date is not set for a document, such a document is considered as always <strong>outside</strong> periods
</span>
</div>
To achieve lists' topicality, the tool let you set up intervals to search documents:
<ul>
<li>Restrict time frames by <strong>any date or datetime</strong> of a target document type. It might be deadline, create or close date, next activity day, etc.</li>
<li>If you wish, apply a few periods based on different dates. For instance, select this month closed leads which have been opened the last year. Records should satisfy <strong>all</strong> of the criteria, however if you selected the same date twice, records should be within <strong>any</strong> of those periods. For example, a deadline should be within the last 2 months OR the next month AND a close date should be within the last year</li>
<li>Periods are relative, so they are <strong>periods in comparison to today</strong>. E.g., 'this month', 'the last year', 'the next 5 weeks'</li>
<li>Intervals may both define previous time frames ('the last') and forthcoming periods ('the next')</li>
<li>As intervals select days, weeks, months, or years</li>
<li>Exclude or include a current period. For example, you might send a reminder on the first day of a month for a previous one. Vice versa, forward a list on the last day of this month for a current one</li>
<li>Test your settings according to a real-time-shown result below the table</li>
</ul>
    # <a name='filtering'></a>Filtering
    <div class="alert alert-danger">
<span style="font-size:18px">
    <i class="fa fa-exclamation-triangle"></i> Apply filters thoroughly: make sure you are not forwarding confidential data to wrong partners
</span>
</div>
Not all, even topical, documents should be included into lists. There is no sense to inform a sales manager about leads of another team. Be especially attentive in case of reminders for external partners: make sure you filter by a related customer. The tool let you do that flexibly:
<ul>
<li>Filters are organized as a domain constructor: you may use the most of storable fields with any level of precision. The latter means, for example, you can filter sales orders by a related partner country or even by a state of a company of a related partner</li>
<li>Use both 'AND' ('all') and 'OR' ('any') operators to achieve a desired result</li>
<li>Check yourself by pressing the button 'Records': it would show all documents which at the moment satisfy your search criteria (and you have an access to)</li>
<li>If you feel confident to prepare Reverse Polish Notation domains, turn on the debug mode, and apply more complex expressions such as, for instance, ' category is child_of all'</li>
</ul>
    # <a name='recurrence'></a>Recurrence
    <div class="alert alert-warning">
<span style="font-size:18px">
    <i class="fa fa-book"></i> Be cautious with a month or year exact date: if it didn't exist, a last month day would be applied: 31/09 --> 30/09
</span>
</div>
It doesn't look fine to send a reminder on Sunday? No problem at all, define regularity in a way you like:
<ul>
<li>Send a reminder every day, each 5 days, each 181 days</li>
<li>Notify by exact weekdays, e.g. on Mondays and Thursdays</li>
<li>For monthly reminders use:
<ul>
<li>The first month day</li>
<li>The last month day</li>
<li>The exact date, e.g. the 16th</li>
<li>A weekday, for instance, the first Monday, the last Friday, or the third Tuesday</li>
</ul>
</li>
<li>Prepare a yearly statistics on an exact year day, e.g. on the first of September</li>
</ul>

    # <a name='user-rights'></a>User rights
    <div class="alert alert-danger">
<span style="font-size:18px">
    <i class="fa fa-exclamation-triangle"></i> Make sure you trust a reminder manager. Such a user will be able to send some documents without a permission for those
</span>
</div>
In the most cases reminders should be prepared by the Odoo SuperAdmin, since it is the only one who has full rights for all models. Simultaneously, the tool let you grant an access to lists for <strong>any user</strong>:
<ul>
<li>To observe the reminders' menu and configure new notifications, select the right 'Lists Reminder Manager' in this user settings</li>
<li>Make sure you trust such a person. This user would be able to send any data by a document type to which he/she has a read access. It means, that if a user might read leads in general, but do not have rights to read the exact lead 'XXX', he/she would be able to send the data by the lead 'XXX' using the reminder</li>
<li>To configure a reminder by this document type, a user should have a read access to such a model. For example, an employee without the right 'Warehouse user' might not prepare a reminder by deliveries</li>
</ul>

    # <a name='use-cases'></a>Use cases
    The tool works for any Odoo document type. It might be sale or purchase orders, leads or tasks, activities or meetings, deliveries or manufacturing operations, thus, generally all models which exist in your system. The module is mostly used:
<ul>
<li>To send periodical statistics for managers</li>
<li>To forward to-do lists for certain actions</li>
<li>To plan forthcoming events and actions</li>
<li>To notify customers or suppliers of done jobs.</li>
</ul>
Please find below a few typical examples.

<p style="padding-top: 10px;"><strong>Pipeline results</strong><i> --> to get leads closed the previous month for a team manager</i></p>
<ul>
<li>Choose Lead/Opportunity as a model</li>
<li>Define a period as Closed Date in the last month</li>
<li>Make a filter Sales Channel > Sales Channel contains 'Europe', where 'Europe' is your sales team</li>
<li>As columns define Display Name, Salesperson > name, Salesperson > phone,  Tags, Expected Revenue</li>
<li>Subscribe a sales team manager for this reminder</li>
<li>Send a list each month, on the first Monday.</li>
</ul>
<p>Similar lists might be configured for sale orders, deliveries, purchase orders, manufacturing operations, etc.</p>

<p style="padding-top: 10px;"><strong>Daily to-do list</strong><i> --> to get activities which should be done today or previously</i></p>
<ul>
<li>Choose Activity as a document type</li>
<li>Define a period as Due Date in the last 10000 days including this (to get even the eldest activities)</li>
<li>Make a filter Assigned to > Name contains 'John Brown', where 'John Brown' is a user to notify</li>
<li>As columns apply Display name, Category, Due Date, Note</li>
<li>Subscribe a John Brown for this reminder</li>
<li>Send a list everyday.</li>
</ul>
<p>Similar reminders are usually prepared for project tasks, opportunities, planned deliveries or incoming shipments, etc.</p>

<div class="alert alert-info">
<span style="font-size:18px">
    <i class="fa fa-info-circle"></i> To prepare the same reminder for another user: duplicate this one, update the filter to a new employee and subscribe him/her
</span>
</div>

<p style="padding-top: 10px;"><strong>Planned events</strong><i> --> to get events which will happen in forthcoming periods</i></p>
<ul>
<li>Choose Event as an object for this reminder</li>
<li>Define a period as Start Date the last week, including this (it would be 'this week'), or the next 3 weeks</li>
<li>Make no filters</li>
<li>As columns apply Event name, Location, Start Date, End Date</li>
<li>Subscribe a John Brown for this reminder, where John Brown is an event department head</li>
<li>Send a list on Mondays.</li>
</ul>
<p>Similar reminders are Okay for activities, tasks, leads, deliveries, incoming shipments, etc.</p>


<p style="padding-top: 10px;"><strong>Customer project statistics</strong><i> --> to notify customers about their tasks</i></p>
<ul>
<li>Choose Task as a target model</li>
<li>Define a period as Create Date in the last year</li>
<li>Make 2 filters: Customer > Parent name is 'Agrolait' or Customer name is 'Agrolait', where 'Agrolait' is project customer</li>
<li>As columns apply Display name, Deadline, Description, Last Stage Update, Stage > display name</li>
<li>Subscribe a John Brown for this reminder, where John Brown is a managing partner of Agrolait</li>
<li>Send a list on the 10th of January each year.</li>
</ul>
<p>Similar statistics is frequently forwarded by support tickets, paid invoices, done sale orders, etc.</p>
    Configure lists of records to be sent according to chosen periods
    Filter Odoo records to be included into a list
    Configure list columns and reminder appearance
    Remind to any user, customer, supplier or send lists to Odoo channels
    Followers regularly receive lists on their email
    The Excel (xlsx) table is optionally attached
    Flexibly configure reminders frequency
    Sent reminder weekly on predefined weekdays
    Define a month day for lists notifications 
    Make reminder monthly on predefined weekdays
    Make any user prepare lists reminders
    Reminder managers may configure lists only for documents they can read
    Good at Odoo domains? Turn on the debug mode
""",
    "images": [
        "static/description/main.png"
    ],
    "price": "172.0",
    "currency": "EUR",
}