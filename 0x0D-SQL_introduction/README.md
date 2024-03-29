<h1 class="gap">0x0D. SQL - Introduction</h1><div class="gap" id="project-description">
<p><img alt="" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg" style=""/></p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a href="/rltoken/khEqMKp1PHvKpfO18d4fLQ" target="_blank" title="What is Database &amp; SQL?">What is Database &amp; SQL?</a> </li>
<li><a href="/rltoken/qrONF5FZPsRxRJ2FkLVPcg" target="_blank" title="A Basic MySQL Tutorial">A Basic MySQL Tutorial</a> </li>
<li><a href="/rltoken/ibCYnC9CDgZg5NQQvccBWw" target="_blank" title="Basic SQL statements: DDL and DML">Basic SQL statements: DDL and DML</a> (<em>no need to read the chapter “Privileges”</em>)</li>
<li><a href="/rltoken/yelYhpf7l0FcRIPCVfnMLw" target="_blank" title="Basic queries: SQL and RA">Basic queries: SQL and RA</a> </li>
<li><a href="/rltoken/3aQcovOE-clrD8yIfxFE9Q" target="_blank" title="SQL technique: functions">SQL technique: functions</a> </li>
<li><a href="/rltoken/lTXnq6pdk59x2h_Y-q0-Hg" target="_blank" title="SQL technique: subqueries">SQL technique: subqueries</a> </li>
<li><a href="/rltoken/R--kAkehyaawZFY4m1inxQ" target="_blank" title="What makes the big difference between a backtick and an apostrophe?">What makes the big difference between a backtick and an apostrophe?</a> </li>
<li><a href="/rltoken/aGZu7ulJpbbKcDhcz49yrg" target="_blank" title="MySQL Cheat Sheet">MySQL Cheat Sheet</a> </li>
<li><a href="/rltoken/XrqR4oh6zsk0eOKoTgkA3Q" target="_blank" title="MySQL 5.7 SQL Statement Syntax">MySQL 5.7 SQL Statement Syntax</a> </li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a href="/rltoken/jfYCdfSeM9SClR9gWzDaLA" target="_blank" title="explain to anyone">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>What’s a database</li>
<li>What’s a relational database</li>
<li>What does SQL stand for</li>
<li>What’s MySQL</li>
<li>How to create a database in MySQL</li>
<li>What does <code>DDL</code> and <code>DML</code> stand for</li>
<li>How to <code>CREATE</code> or <code>ALTER</code> a table</li>
<li>How to <code>SELECT</code> data from a table</li>
<li>How to <code>INSERT</code>, <code>UPDATE</code> or <code>DELETE</code> data</li>
<li>What are <code>subqueries</code></li>
<li>How to use MySQL functions</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be executed on Ubuntu 14.04 LTS using <code>MySQL 5.7</code> (version 5.7.8-rc)</li>
<li>All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>, <code>WHERE</code>…)</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>
<h2>More Info</h2>
<h3>Comments for your SQL file:</h3>
<pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>
<h3>Install MySQL 5.7 on Ubuntu 14.04 LTS</h3>
<pre><code>$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$
</code></pre>
<p><strong>Don’t forget your <code>root</code> password</strong></p>
<p>Connect to your MySQL server:</p>
<pre><code>$ mysql -hlocalhost -uroot -p
Password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 42
Server version: 5.7.8-rc MySQL Community Server (GPL)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql&gt; 
mysql&gt; quit
Bye
$
</code></pre>
<p>If you have some issues to upgrade to 5.7, don’t hesitate to cleanup your server of any MySQL packages: <code>sudo apt-get remove --purge mysql-server mysql-client mysql-common</code></p>
<h3>Use “container-on-demand” to run MySQL</h3>
<ul>
<li>Ask for container <code>Ubuntu 14.04 - Python 3.4</code></li>
<li>Connect via SSH</li>
<li>OR connect via the Web terminal</li>
<li>In the container, you should start MySQL before playing with it:</li>
</ul>
<pre><code>$ service mysql start
 * MySQL Community Server 5.7.8-rc is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
</code></pre>
<p><strong>In the container, credentials are <code>root/root</code></strong></p>
</div>