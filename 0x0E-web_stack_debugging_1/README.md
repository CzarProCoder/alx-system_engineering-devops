<h1>0x0E. Web stack debugging #1</h1>
<div>
    <div>DevOpsSysAdminScriptingDebugging</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Sylvain Kalache</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Project will start&nbsp;<span title="">Jul 3, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Jul 7, 2023 6:00 AM</span></li>
        <li>&nbsp;Checker&nbsp;was&nbsp;released at&nbsp;<span title="">Jul 5, 2023 8:24 PM</span></li>
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
            <li><a href="https://intranet.alxswe.com/concepts/33">Network basics</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/68">Web stack debugging</a></li>
        </ul>
    </div>
</div>
<div>
    <div>
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/271/B4eeypV.jpg" alt=""></p>
        <h2>Requirements</h2>
        <h3>General</h3>
        <ul>
            <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
            <li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
            <li>All your files should end with a new line</li>
            <li>A&nbsp;<code>README.md</code> file at the root of the folder of the project is mandatory</li>
            <li>All your Bash script files must be executable</li>
            <li>Your Bash scripts must pass&nbsp;<code>Shellcheck</code> without any error</li>
            <li>Your Bash scripts must run without error</li>
            <li>The first line of all your Bash scripts should be exactly&nbsp;<code>#!/usr/bin/env bash</code></li>
            <li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
            <li>You are not allowed to use&nbsp;<code>wget</code></li>
        </ul>
    </div>
</div>
<h2>Tasks</h2>
<div>
    <div>
        <div>
            <h3>0. Nginx likes port 80</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Using your debugging skills, find out what&rsquo;s keeping your Ubuntu container&rsquo;s Nginx installation from listening on port&nbsp;<code>80</code>. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.</p>
            <p>Requirements:</p>
            <ul>
                <li>Nginx must be running, and listening on port&nbsp;<code>80</code> of all the server&rsquo;s active IPv4 IPs</li>
                <li>Write a Bash script that configures a server to the above requirements</li>
            </ul>
            <pre><code>root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# ./0-nginx_likes_port_80 &gt; /dev/null 2&amp;&gt;1
root@966c5664b21f:/#
root@966c5664b21f:/# curl 0:80
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;title&gt;Welcome to nginx!&lt;/title&gt;
&lt;style&gt;
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;Welcome to nginx!&lt;/h1&gt;
&lt;p&gt;If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.&lt;/p&gt;

&lt;p&gt;For online documentation and support please refer to
&lt;a href=&quot;http://nginx.org/&quot;&gt;nginx.org&lt;/a&gt;.&lt;br/&gt;
Commercial support is available at
&lt;a href=&quot;http://nginx.com/&quot;&gt;nginx.com&lt;/a&gt;.&lt;/p&gt;

&lt;p&gt;&lt;em&gt;Thank you for using nginx.&lt;/em&gt;&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
root@966c5664b21f:/#
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x0E-web_stack_debugging_1</code></li>
                    <li>File:&nbsp;<code>0-nginx_likes_port_80</code></li>
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
            <h3>1. Make it sweet and short</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Using what you did for task #0, make your fix short and sweet.</p>
            <p>Requirements:</p>
            <ul>
                <li>Your Bash script must be 5 lines long or less</li>
                <li>There must be a new line at the end of the file</li>
                <li>You must respect usual Bash script requirements</li>
                <li>You cannot use&nbsp;<code>;</code></li>
                <li>You cannot use&nbsp;<code>&amp;&amp;</code></li>
                <li>You cannot use&nbsp;<code>wget</code></li>
                <li>You cannot execute your previous answer file (Do not include the name of the previous script in this one)</li>
                <li><code>service</code> (init) must say that&nbsp;<code>nginx</code> is not running &larr; for real</li>
            </ul>
            <pre><code>root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# cat -e 1-debugging_made_short | wc -l
5
root@966c5664b21f:/# ./1-debugging_made_short
root@966c5664b21f:/# curl 0:80
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;title&gt;Welcome to nginx!&lt;/title&gt;
&lt;style&gt;
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;Welcome to nginx!&lt;/h1&gt;
&lt;p&gt;If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.&lt;/p&gt;

&lt;p&gt;For online documentation and support please refer to
&lt;a href=&quot;http://nginx.org/&quot;&gt;nginx.org&lt;/a&gt;.&lt;br/&gt;
Commercial support is available at
&lt;a href=&quot;http://nginx.com/&quot;&gt;nginx.com&lt;/a&gt;.&lt;/p&gt;

&lt;p&gt;&lt;em&gt;Thank you for using nginx.&lt;/em&gt;&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
root@966c5664b21f:/#
root@966c5664b21f:/# service nginx status
 * nginx is not running
root@966c5664b21f:/# 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x0E-web_stack_debugging_1</code></li>
                    <li>File:&nbsp;<code>1-debugging_made_short</code></li>
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