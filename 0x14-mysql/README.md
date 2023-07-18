<h1>0x14. MySQL</h1>
<div>
    <div>DevOpsSysAdminMySQL</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Sylvain Kalache, co-founder at Holberton School</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Project will start&nbsp;<span title="">Jul 18, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Jul 19, 2023 6:00 AM</span></li>
        <li>&nbsp;Checker&nbsp;was&nbsp;released at&nbsp;<span title="">Jul 18, 2023 12:00 PM</span></li>
        <li>&nbsp;An auto review will be launched at the deadline</li>
    </ul>
</div>
<div>
    <div>
        <h3>Concepts</h3>
    </div>
    <div>
        <p><em>For this project, we expect you to look at these concepts:</em></p>
        <ul>
            <li><a href="https://intranet.alxswe.com/concepts/49">Database administration</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/68">Web stack debugging</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/100002">[How to] Install mysql 5.7</a></li>
        </ul>
    </div>
</div>
<div>
    <div>
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/280/KkrkDHT.png" alt=""></p>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/eojqG9FZbA6QVWN5P9cLzA" title="What is a primary-replica cluster" target="_blank">What is a primary-replica cluster</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/z2KVk2UKLMc0RvHMdJmYLg" title="MySQL primary replica setup" target="_blank">MySQL primary replica setup</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/BharnxaLb-BDDYFywzME2Q" title="Build a robust database backup strategy" target="_blank">Build a robust database backup strategy</a></li>
        </ul>
        <p><strong>man or help</strong>:</p>
        <ul>
            <li><code>mysqldump</code></li>
        </ul>
        <h2>Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/Lotf0yqq3mNeFHkrW67CZQ" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
        <h3>General</h3>
        <ul>
            <li>What is the main role of a database</li>
            <li>What is a database replica</li>
            <li>What is the purpose of a database replica</li>
            <li>Why database backups need to be stored in different physical locations</li>
            <li>What operation should you regularly perform to make sure that your database backup strategy actually works</li>
        </ul>
        <h3>Copyright - Plagiarism</h3>
        <ul>
            <li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
            <li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else&rsquo;s work.</li>
            <li>You are not allowed to publish any content of this project.</li>
            <li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
        </ul>
        <h2>Requirements</h2>
        <h3>General</h3>
        <ul>
            <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
            <li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
            <li>All your files should end with a new line</li>
            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>All your Bash script files must be executable</li>
            <li>Your Bash script must pass&nbsp;<code>Shellcheck</code> (version&nbsp;<code>0.3.7-5~ubuntu16.04.1</code> via&nbsp;<code>apt-get</code>) without any error</li>
            <li>The first line of all your Bash scripts should be exactly&nbsp;<code>#!/usr/bin/env bash</code></li>
            <li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
        </ul>
    </div>
</div>
<h2>Your servers</h2>
<div>
    <div>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Username</th>
                    <th>IP</th>
                    <th>State</th>
                    <th><br></th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>196617-web-01</td>
                    <td><code>ubuntu</code></td>
                    <td><code>54.85.205.43</code></td>
                    <td>running</td>
                    <td>
                        <div><button type="button">Actions&nbsp;Toggle Dropdown</button></div>
                    </td>
                </tr>
                <tr>
                    <td>196617-web-02</td>
                    <td><code>ubuntu</code></td>
                    <td><code>3.85.136.55</code></td>
                    <td>running</td>
                    <td>
                        <div><button type="button">Actions&nbsp;Toggle Dropdown</button></div>
                    </td>
                </tr>
                <tr>
                    <td>196617-lb-01</td>
                    <td><code>ubuntu</code></td>
                    <td><code>18.234.80.159</code></td>
                    <td>running</td>
                    <td>
                        <div><button type="button">Actions&nbsp;Toggle Dropdown</button></div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
<h2>Tasks</h2>
<div>
    <div>
        <div>
            <h3>0. Install MySQL</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>First things first, let&rsquo;s get MySQL installed on&nbsp;<strong>both</strong> your web-01 and web-02 servers.</p>
            <ul>
                <li>MySQL distribution must be 5.7.x</li>
                <li>Make sure that&nbsp;<a href="https://intranet.alxswe.com/rltoken/h8QknQcmmLf7oT8esoWgvg" title="task #3" target="_blank">task #3</a> of your&nbsp;<a href="https://intranet.alxswe.com/rltoken/Wx_BrR5Sk8s3Ywl44-33wg" title="SSH project" target="_blank">SSH project</a> is completed for&nbsp;<code>web-01</code> and&nbsp;<code>web-02</code>. The checker will connect to your servers to check MySQL status</li>
                <li>Please make sure you have your&nbsp;<code>README.md</code> pushed to GitHub.</li>
            </ul>
            <p>Example:</p>
            <pre><code>ubuntu@229-web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
ubuntu@229-web-01:~$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x14-mysql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>1. Let us in!</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>In order for us to verify that your servers are properly configured, we need you to create a user and password for&nbsp;<strong>both</strong> MySQL databases which will allow the checker access to them.</p>
            <ul>
                <li>Create a MySQL user named&nbsp;<code>holberton_user</code> on both&nbsp;<code>web-01</code> and&nbsp;<code>web-02</code> with the host name set to&nbsp;<code>localhost</code> and the password&nbsp;<code>projectcorrection280hbtn</code>. This will allow us to access the replication status on both servers.</li>
                <li>Make sure that&nbsp;<code>holberton_user</code> has permission to check the primary/replica status of your databases.</li>
                <li>In addition to that, make sure that&nbsp;<a href="https://intranet.alxswe.com/rltoken/h8QknQcmmLf7oT8esoWgvg" title="task #3" target="_blank">task #3</a> of your&nbsp;<a href="https://intranet.alxswe.com/rltoken/Wx_BrR5Sk8s3Ywl44-33wg" title="SSH project" target="_blank">SSH project</a> is completed for&nbsp;<code>web-01</code> and&nbsp;<code>web-02</code>.&nbsp;<strong>You will likely need to add the public key to web-02 as you only added it to web-01 for this project.</strong> The checker will connect to your servers to check MySQL status</li>
            </ul>
            <p>Example:</p>
            <pre><code>ubuntu@229-web-01:~$ mysql -uholberton_user -p -e &quot;SHOW GRANTS FOR &apos;holberton_user&apos;@&apos;localhost&apos;&quot;
Enter password:
+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO &apos;holberton_user&apos;@&apos;localhost&apos; |
+-----------------------------------------------------------------+
ubuntu@229-web-01:~$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x14-mysql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>2. If only you could see what I&apos;ve seen with your eyes</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>In order for you to set up replication, you&rsquo;ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.</p>
            <ul>
                <li>Create a database named&nbsp;<code>tyrell_corp</code>.</li>
                <li>Within the&nbsp;<code>tyrell_corp</code> database create a table named&nbsp;<code>nexus6</code> and add at least one entry to it.</li>
                <li>Make sure that&nbsp;<code>holberton_user</code> has&nbsp;<code>SELECT</code> permissions on your table so that we can check that the table exists and is not empty.</li>
            </ul>
            <pre><code>ubuntu@229-web-01:~$ mysql -uholberton_user -p -e &quot;use tyrell_corp; select * from nexus6&quot;
Enter password:
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
ubuntu@229-web-01:~$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x14-mysql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>3. Quite an experience to live in fear, isn&apos;t it?</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Before you get started with your primary-replica synchronization, you need one more thing in place. On your&nbsp;<strong>primary</strong> MySQL server (web-01), create a new user for the replica server.</p>
            <ul>
                <li>The name of the new user should be&nbsp;<code>replica_user</code>, with the host name set to&nbsp;<code>%</code>, and can have whatever password you&rsquo;d like.</li>
                <li><code>replica_user</code> must have the appropriate permissions to replicate your primary MySQL server.</li>
                <li><code>holberton_user</code> will need SELECT privileges on the&nbsp;<code>mysql.user</code> table in order to check that&nbsp;<code>replica_user</code> was created with the correct permissions.</li>
            </ul>
            <pre><code>ubuntu@229-web-01:~$ mysql -uholberton_user -p -e &apos;SELECT user, Repl_slave_priv FROM mysql.user&apos;
+------------------+-----------------+
| user             | Repl_slave_priv |
+------------------+-----------------+
| root             | Y               |
| mysql.session    | N               |
| mysql.sys        | N               |
| debian-sys-maint | Y               |
| holberton_user   | N               |
| replica_user     | Y               |
+------------------+-----------------+
ubuntu@229-web-01:~$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x14-mysql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>4. Setup a Primary-Replica infrastructure using MySQL</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/09e83e914f0d6865ce320a47f2f14837a5b190b6.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230718%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230718T101621Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7d38d257277d10322c504e6b67d60c38e9374f63742c77a3e9d91b175379b429" alt=""></p>
            <p>Having a replica member on for your MySQL database has 2 advantages:</p>
            <ul>
                <li>Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data</li>
                <li>Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed</li>
            </ul>
            <h3>Requirements:</h3>
            <ul>
                <li>MySQL primary must be hosted on&nbsp;<code>web-01</code> - do not use the&nbsp;<code>bind-address</code>, just comment out this parameter</li>
                <li>MySQL replica must be hosted on&nbsp;<code>web-02</code></li>
                <li>Setup replication for the MySQL database named&nbsp;<code>tyrell_corp</code></li>
                <li>Provide your MySQL primary configuration as answer file(<code>my.cnf</code> or&nbsp;<code>mysqld.cnf</code>) with the name&nbsp;<code>4-mysql_configuration_primary</code></li>
                <li>Provide your MySQL replica configuration as an answer file with the name&nbsp;<code>4-mysql_configuration_replica</code></li>
            </ul>
            <h3>Tips:</h3>
            <ul>
                <li>Once MySQL replication is setup, add a new record in your table via MySQL on&nbsp;<code>web-01</code> and check if the record has been replicated in MySQL&nbsp;<code>web-02</code>. If you see it, it means your replication is working!</li>
                <li><strong>Make sure that UFW is allowing connections on port 3306 (default MySQL port) otherwise replication will not work</strong>.</li>
            </ul>
            <p>Example:</p>
            <h2><code>web-01</code></h2>
            <pre><code>ubuntu@web-01:~$ mysql -uholberton_user -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1467
Server version: 5.5.49-0ubuntu0.14.04.1-log (Ubuntu)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type &apos;help;&apos; or &apos;\h&apos; for help. Type &apos;\c&apos; to clear the current input statement.

mysql&gt; show master status;
+------------------+----------+--------------------+------------------+
| File             | Position | Binlog_Do_DB       | Binlog_Ignore_DB |
+------------------+----------+--------------------+------------------+
| mysql-bin.000009 |      107 | tyrell_corp          |                  |
+------------------+----------+--------------------+------------------+
1 row in set (0.00 sec)

mysql&gt; 
</code></pre>
            <h2><code>web-02</code></h2>
            <pre><code>root@web-02:/home/ubuntu# mysql -uholberton_user -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 53
Server version: 5.5.49-0ubuntu0.14.04.1-log (Ubuntu)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type &apos;help;&apos; or &apos;\h&apos; for help. Type &apos;\c&apos; to clear the current input statement.

mysql&gt; show slave status\G
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 158.69.68.78
                  Master_User: replica_user
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000009
          Read_Master_Log_Pos: 107
               Relay_Log_File: mysql-relay-bin.000022
                Relay_Log_Pos: 253
        Relay_Master_Log_File: mysql-bin.000009
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB: 
          Replicate_Ignore_DB: 
           Replicate_Do_Table: 
       Replicate_Ignore_Table: 
      Replicate_Wild_Do_Table: 
  Replicate_Wild_Ignore_Table: 
                   Last_Errno: 0
                   Last_Error: 
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 107
              Relay_Log_Space: 452
              Until_Condition: None
               Until_Log_File: 
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File: 
           Master_SSL_CA_Path: 
              Master_SSL_Cert: 
            Master_SSL_Cipher: 
               Master_SSL_Key: 
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error: 
               Last_SQL_Errno: 0
               Last_SQL_Error: 
  Replicate_Ignore_Server_Ids: 
             Master_Server_Id: 1
1 row in set (0.00 sec)

mysql&gt; 

</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x14-mysql</code></li>
                    <li>File:&nbsp;<code>4-mysql_configuration_primary, 4-mysql_configuration_replica</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>5. MySQL backup</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p><a href="https://www.youtube.com/watch?v=ANU-oSE5_hU" target="_blank"><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/280/Bbpsgif.jpg" alt=""></a></p>
            <p>What if the data center where both your primary and replica database servers are hosted are down because of a power outage or even worse: flooding, fire? Then all your data would inaccessible or lost. That&rsquo;s why you want to backup and store them in a different system in another physical location. This can be achieved by dumping your MySQL data, compressing them and storing them in a different data center.</p>
            <p>Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.</p>
            <p>Requirements:</p>
            <ul>
                <li>The MySQL dump must contain all your MySQL databases</li>
                <li>The MySQL dump must be named&nbsp;<code>backup.sql</code></li>
                <li>The MySQL dump file has to be compressed to a&nbsp;<code>tar.gz</code> archive</li>
                <li>This archive must have the following name format:&nbsp;<code>day-month-year.tar.gz</code></li>
                <li>The user to connect to the MySQL database must be&nbsp;<code>root</code></li>
                <li>The Bash script accepts one argument that is the password used to connect to the MySQL database</li>
            </ul>
            <p>Example:</p>
            <pre><code>ubuntu@03-web-01:~$ ls
5-mysql_backup
ubuntu@03-web-01:~$ ./5-mysql_backup mydummypassword
backup.sql
ubuntu@03-web-01:~$ ls
01-03-2017.tar.gz  5-mysql_backup  backup.sql
ubuntu@03-web-01:~$ more backup.sql
-- MySQL dump 10.13  Distrib 5.7.25, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database:
-- ------------------------------------------------------
-- Server version   5.7.25-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE=&apos;+00:00&apos; */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE=&apos;NO_AUTO_VALUE_ON_ZERO&apos; */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `tyrell_corp`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `tyrell_corp` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `tyrell_corp`;

--
-- Table structure for table `nexus6`
--

DROP TABLE IF EXISTS `nexus6`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nexus6` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `firstname` varchar(30) NOT NULL,
  `lastname` varchar(30) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `reg_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
ubuntu@03-web-01:~$
ubuntu@03-web-01:~$ file 01-03-2017.tar.gz
01-03-2017.tar.gz: gzip compressed data, from Unix, last modified: Wed Mar  1 23:38:09 2017
ubuntu@03-web-01:~$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x14-mysql</code></li>
                    <li>File:&nbsp;<code>5-mysql_backup</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button>&nbsp;</div>
            </div>
        </div>
    </div>
</div>
