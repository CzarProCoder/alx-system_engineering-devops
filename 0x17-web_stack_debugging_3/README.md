<h1>0x17. Web stack debugging #3</h1>
<div>
    <div>DevOpsSysAdminScriptingDebugging</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Sylvain Kalache, co-founder at Holberton School</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Project will start&nbsp;<span title="">Aug 8, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Aug 10, 2023 6:00 AM</span></li>
        <li>&nbsp;Checker&nbsp;was&nbsp;released at&nbsp;<span title="">Aug 9, 2023 1:12 PM</span></li>
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
            <li><a href="https://intranet.alxswe.com/concepts/17">Web Server</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/68">Web stack debugging</a></li>
        </ul>
    </div>
</div>
<div>
    <div>
        <h2>Background Context</h2>
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png" alt=""></p>
        <p>When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)</p>
        <p>Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites&hellip; It&nbsp;<a href="https://intranet.alxswe.com/rltoken/qxyFYZIwOXQWw02-HaQ7Bw" title="actually powers 26% of the web" target="_blank">actually powers 26% of the web</a>, so there is a fair chance that you will end up working with it at some point in your career.</p>
        <p>Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.</p>
        <p>The web stack you are debugging today is a Wordpress website running on a LAMP stack.</p>
        <h2>Requirements</h2>
        <h3>General</h3>
        <ul>
            <li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
            <li>All your files should end with a new line</li>
            <li>A&nbsp;<code>README.md</code> file at the root of the folder of the project is mandatory</li>
            <li>Your Puppet manifests must pass&nbsp;<code>puppet-lint</code> version 2.1.1 without any errors</li>
            <li>Your Puppet manifests must run without error</li>
            <li>Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about</li>
            <li>Your Puppet manifests files must end with the extension&nbsp;<code>.pp</code></li>
            <li>Files will be checked with Puppet v3.4</li>
        </ul>
        <h2>More Info</h2>
        <h3>Install&nbsp;<code>puppet-lint</code></h3>
        <pre><code>$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
</code></pre>
    </div>
</div>
<h2>Tasks</h2>
<div>
    <div>
        <div>
            <h3>0. Strace is your friend</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p><a href="https://youtu.be/uHEzt1QuASo" target="_blank"><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/f5af5167e65bd3101f76.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230809%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230809T184333Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a94a5a5aaa38d1f7dbc0d8f0af73c41d63b83f33edd98225d50eea020895f5d4" alt=""></a></p>
            <p>Using&nbsp;<code>strace</code>, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).</p>
            <p>Hint:</p>
            <ul>
                <li><code>strace</code> can attach to a current running process</li>
                <li>You can use&nbsp;<a href="https://intranet.alxswe.com/rltoken/UsSRoxIYdq0l0QUIuDNnSw" title="tmux" target="_blank">tmux</a> to run&nbsp;<a href="https://intranet.alxswe.com/rltoken/ueMevAif95DjyW2sqVCMoA" title="strace" target="_blank">strace</a> in one window and&nbsp;<code>curl</code> in another one</li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>Your&nbsp;<code>0-strace_is_your_friend.pp</code> file must contain Puppet code</li>
                <li>You can use whatever Puppet resource type you want for you fix</li>
            </ul>
            <p>Example:</p>
            <pre><code>root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
root@e514b399d69d:~#
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: &lt;http://127.0.0.1/?rest_route=/&gt;; rel=&quot;https://api.w.org/&quot;
Content-Type: text/html; charset=UTF-8

root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
&lt;title&gt;Holberton &amp;#8211; Just another WordPress site&lt;/title&gt;
&lt;link rel=&quot;alternate&quot; type=&quot;application/rss+xml&quot; title=&quot;Holberton &amp;raquo; Feed&quot; href=&quot;http://127.0.0.1/?feed=rss2&quot; /&gt;
&lt;link rel=&quot;alternate&quot; type=&quot;application/rss+xml&quot; title=&quot;Holberton &amp;raquo; Comments Feed&quot; href=&quot;http://127.0.0.1/?feed=comments-rss2&quot; /&gt;
        &lt;div id=&quot;wp-custom-header&quot; class=&quot;wp-custom-header&quot;&gt;&lt;img src=&quot;http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg&quot; width=&quot;2000&quot; height=&quot;1200&quot; alt=&quot;Holberton&quot; /&gt;&lt;/div&gt;  &lt;/div&gt;
                            &lt;h1 class=&quot;site-title&quot;&gt;&lt;a href=&quot;http://127.0.0.1/&quot; rel=&quot;home&quot;&gt;Holberton&lt;/a&gt;&lt;/h1&gt;
        &lt;p&gt;Yet another bug by a Holberton student&lt;/p&gt;
root@e514b399d69d:~#
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x17-web_stack_debugging_3</code></li>
                    <li>File:&nbsp;<code>0-strace_is_your_friend.pp</code></li>
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
<div>
    <div>
        <div>
            <div><br></div>
        </div>
    </div>
</div>
