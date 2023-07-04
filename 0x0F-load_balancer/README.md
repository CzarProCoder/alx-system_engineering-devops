<h1>0x0F. Load balancer</h1>
<div>
    <div>DevOpsSysAdmin</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Sylvain Kalache, co-founder at Holberton School</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Ongoing second chance project - started&nbsp;<span title="">Jul 3, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Jul 5, 2023 6:00 AM</span></li>
        <li>&nbsp;An auto review will be launched at the deadline</li>
    </ul>
</div>
<div>
    <h4>In a nutshell&hellip;</h4>
    <ul>
        <li><strong>Auto QA review:</strong> 0.0/4 mandatory &amp; 0.0/2 optional</li>
        <li><strong>Altogether:</strong>&nbsp; <strong>0.0%</strong>
            <ul>
                <li>Mandatory: 0.0%</li>
                <li>Optional: 0.0%</li>
                <li>Calculation: &nbsp;0.0% + (0.0% * 0.0%) &nbsp;== <strong>0.0%</strong></li>
            </ul>
        </li>
    </ul>
</div>
<div>
    <div>
        <h3>Concepts</h3>
    </div>
    <div>
        <p><em>For this project, we expect you to look at these concepts:</em></p>
        <ul>
            <li><a href="https://intranet.alxswe.com/concepts/46">Load balancer</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/68">Web stack debugging</a></li>
        </ul>
    </div>
</div>
<div>
    <div>
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png" alt=""></p>
        <h2>Background Context</h2>
        <p>You have been given 2 additional servers:</p>
        <ul>
            <li>gc-[STUDENT_ID]-web-02-XXXXXXXXXX</li>
            <li>gc-[STUDENT_ID]-lb-01-XXXXXXXXXX</li>
        </ul>
        <p>Let&rsquo;s improve our web stack so that there is&nbsp;<a href="https://intranet.alxswe.com/rltoken/xnAaJdhmAxx7PoH3l6EwDg" title="redundancy" target="_blank">redundancy</a> for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.</p>
        <p>For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.</p>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/B7f3oz8i3Xvvom_YQZzLnQ" title="Introduction to load-balancing and HAproxy" target="_blank">Introduction to load-balancing and HAproxy</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/sZ9v3Vq2tgLwN_PWVQketw" title="HTTP header" target="_blank">HTTP header</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/2VRAgtKKR9g6Xfb0xzGiSg" title="Debian/Ubuntu HAProxy packages" target="_blank">Debian/Ubuntu HAProxy packages</a></li>
        </ul>
        <h2>Requirements</h2>
        <h3>General</h3>
        <ul>
            <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
            <li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
            <li>All your files should end with a new line</li>
            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>All your Bash script files must be executable</li>
            <li>Your Bash script must pass&nbsp;<code>Shellcheck</code> (version&nbsp;<code>0.3.7</code>) without any error</li>
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
                    <td><code>107.23.233.224</code></td>
                    <td>running</td>
                    <td>
                        <div><button type="button">Actions&nbsp;Toggle Dropdown</button></div>
                    </td>
                </tr>
                <tr>
                    <td>196617-lb-01</td>
                    <td><br></td>
                    <td><br></td>
                    <td><br></td>
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
            <h3>0. Double the number of webservers</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>In this first task you need to configure&nbsp;<code>web-02</code> to be identical to&nbsp;<code>web-01</code>. Fortunately, you built a Bash script during your&nbsp;<a href="https://intranet.alxswe.com/rltoken/-JluPVwfvXMOYMzNOqvgsQ" title="web server project" target="_blank">web server project</a>, and they&rsquo;ll now come in handy to easily configure&nbsp;<code>web-02</code>. Remember, always try to automate your work!</p>
            <p>Since we&rsquo;re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.</p>
            <p>Requirements:</p>
            <ul>
                <li>Configure Nginx so that its HTTP response contains a custom header (on&nbsp;<code>web-01</code> and&nbsp;<code>web-02</code>)<ul>
                        <li>The name of the custom HTTP header must be&nbsp;<code>X-Served-By</code></li>
                        <li>The value of the custom HTTP header must be the hostname of the server Nginx is running on</li>
                    </ul>
                </li>
                <li>Write&nbsp;<code>0-custom_http_response_header</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task<ul>
                        <li><a href="https://intranet.alxswe.com/rltoken/k3Bt6zu1On_-mDszxi0Z9w" title="Ignore" target="_blank">Ignore</a> <a href="https://intranet.alxswe.com/rltoken/9KwKHb9H8OJqcSK0saRIOA" title="SC2154" target="_blank">SC2154</a> for&nbsp;<code>shellcheck</code></li>
                    </ul>
                </li>
            </ul>
            <p>Example:</p>
            <pre><code>sylvain@ubuntu$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
sylvain@ubuntu$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
sylvain@ubuntu$
</code></pre>
            <p>If your server&rsquo;s hostnames are not properly configured (<code>[STUDENT_ID]-web-01</code> and&nbsp;<code>[STUDENT_ID]-web-02</code>.), follow this&nbsp;<a href="https://intranet.alxswe.com/rltoken/qSor8ulAHl4HedrO6KJEoQ" title="tutorial" target="_blank">tutorial</a>.</p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x0F-load_balancer</code></li>
                    <li>File:&nbsp;<code>0-custom_http_response_header</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>1. Install your load balancer</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Install and configure HAproxy on your&nbsp;<code>lb-01</code> server.</p>
            <p>Requirements:</p>
            <ul>
                <li>Configure HAproxy so that it send traffic to&nbsp;<code>web-01</code> and&nbsp;<code>web-02</code></li>
                <li>Distribute requests using a roundrobin algorithm</li>
                <li>Make sure that HAproxy can be managed via an init script</li>
                <li>Make sure that your servers are configured with the right hostnames:&nbsp;<code>[STUDENT_ID]-web-01</code> and&nbsp;<code>[STUDENT_ID]-web-02</code>. If not, follow this&nbsp;<a href="https://intranet.alxswe.com/rltoken/YkfzgEa6xNHrQbkKmJN4zg" title="tutorial" target="_blank">tutorial</a>.</li>
                <li>For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements</li>
            </ul>
            <p>Example:</p>
            <pre><code>sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:17 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: &quot;58abea7c-1e&quot;
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:19 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: &quot;5315bd25-264&quot;
X-Served-By: 03-web-02
Accept-Ranges: bytes

sylvain@ubuntu$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x0F-load_balancer</code></li>
                    <li>File:&nbsp;<code>1-install_load_balancer</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>2. Add a custom HTTP header with Puppet</h3>
            <div>#advanced</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Just as in task #0, we&rsquo;d like you to automate the task of creating a custom HTTP header response, but with Puppet.</p>
            <ul>
                <li>The name of the custom HTTP header must be&nbsp;<code>X-Served-By</code></li>
                <li>The value of the custom HTTP header must be the hostname of the server Nginx is running on</li>
                <li>Write&nbsp;<code>2-puppet_custom_http_response_header.pp</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
            </ul>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x0F-load_balancer</code></li>
                    <li>File:&nbsp;<code>2-puppet_custom_http_response_header.pp</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button>&nbsp;</div>
            </div>
        </div>
    </div>
</div>
