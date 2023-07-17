<h1>0x12. Web stack debugging #2</h1>
<div>
    <div>DevOpsSysAdminScriptingDebugging</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Sylvain Kalache, co-founder at Holberton School</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Project will start&nbsp;<span title="">Jul 17, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Jul 19, 2023 6:00 AM</span></li>
        <li>&nbsp;Checker&nbsp;will be&nbsp;released at&nbsp;<span title="">Jul 18, 2023 1:12 PM</span></li>
        <li>&nbsp;An auto review will be launched at the deadline</li>
    </ul>
</div>
<div>
    <div>
        <h3>Concepts</h3>
    </div>
    <div>
        <p><em>For this project, we expect you to look at this concept:</em></p>
        <ul>
            <li><a href="https://intranet.alxswe.com/concepts/68">Web stack debugging</a></li>
        </ul>
    </div>
</div>
<div>
    <div>
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/287/99littlebugsinthecode-holberton.jpg" alt=""></p>
        <h2>Requirements</h2>
        <h3>General</h3>
        <ul>
            <li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
            <li>All your files should end with a new line</li>
            <li>A README.md file at the root of the folder of the project is mandatory</li>
            <li>All your Bash script files must be executable</li>
            <li>Your Bash scripts must pass&nbsp;<code>Shellcheck</code> without any error</li>
            <li>Your Bash scripts must run without error</li>
            <li>The first line of all your Bash scripts should be exactly&nbsp;<code>#!/usr/bin/env bash</code></li>
            <li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
        </ul>
    </div>
</div>
<h2>Tasks</h2>
<div>
    <div>
        <div>
            <h3>0. Run software as another user</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/eaeff07a715ff880b1ceb8e863a1d141a74a7f85.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230717%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230717T133725Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=dbfae0bd38ead5c3b49f7a7763812a066f9fb9945fd31df703705688075fb4f6" alt=""></p>
            <p>The user&nbsp;<code>root</code> is, on Linux, the &ldquo;superuser&rdquo;. It can do anything it wants, that&rsquo;s a good and bad thing. A good practice is that one should never be logged in the&nbsp;<code>root</code> user, as if you fat finger a command and for example run&nbsp;<code>rm -rf /</code>, there is no comeback. That&rsquo;s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the&nbsp;<code>root</code> user can do, just need to use a specific command that you need to discover.</p>
            <p>For the containers that you are given in this project as well as the checker, everything is run under the&nbsp;<code>root</code> user, which has the ability to run anything as another user.</p>
            <p>Requirements:</p>
            <ul>
                <li>write a Bash script that accepts one argument</li>
                <li>the script should run the&nbsp;<code>whoami</code> command under the user passed as an argument</li>
                <li>make sure to try your script by passing different users</li>
            </ul>
            <p>Example:</p>
            <pre><code>root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x12-web_stack_debugging_2</code></li>
                    <li>File:&nbsp;<code>0-iamsomeoneelse</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>1. Run Nginx as Nginx</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>The&nbsp;<code>root</code> user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an attacker from logging in as&nbsp;<code>root</code>. With this in mind, it&rsquo;s a good practice not to run your web servers as&nbsp;<code>root</code> (which is the default for most configurations) and instead run the process as the less privileged&nbsp;<code>nginx</code> user instead. This way, if a hacker does find a security issue that allows them to break-in to your server, the impact is limited by the permissions of the&nbsp;<code>nginx</code> user.</p>
            <p>Fix this container so that Nginx is running as the&nbsp;<code>nginx</code> user.</p>
            <p>Requirements:</p>
            <ul>
                <li><code>nginx</code> must be running as&nbsp;<code>nginx</code> user</li>
                <li><code>nginx</code> must be listening on all active IPs on port&nbsp;<code>8080</code></li>
                <li>You cannot use&nbsp;<code>apt-get remove</code></li>
                <li>Write a Bash script that configures the container to fit the above requirements</li>
            </ul>
            <p>After debugging:</p>
            <pre><code>root@ab6f4542747e:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@ab6f4542747e:~#
root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:~#
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x12-web_stack_debugging_2</code></li>
                    <li>File:&nbsp;<code>1-run_nginx_as_nginx</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>2. 7 lines or less</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Using what you did for task #1, make your fix short and sweet.</p>
            <p>Requirements:</p>
            <ul>
                <li>Your Bash script must be 7 lines long or less</li>
                <li>There must be a new line at the end of the file</li>
                <li>You respect Bash script requirements</li>
                <li>You cannot use&nbsp;<code>;</code></li>
                <li>You cannot use&nbsp;<code>&amp;&amp;</code></li>
                <li>You cannot use&nbsp;<code>wget</code></li>
                <li>You cannot execute your previous answer file (Do not include the name of the previous script in this one)</li>
            </ul>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x12-web_stack_debugging_2</code></li>
                    <li>File:&nbsp;<code>100-fix_in_7_lines_or_less</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button>&nbsp;</div>
            </div>
        </div>
    </div>
</div>
