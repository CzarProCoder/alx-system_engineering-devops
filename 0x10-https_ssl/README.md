<h1>0x10. HTTPS SSL</h1>
<div>
    <div>DevOpsSysAdminSecurity</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Sylvain Kalache, co-founder at Holberton School</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Ongoing second chance project - started&nbsp;<span title="">Jul 6, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Jul 8, 2023 6:00 AM</span></li>
        <li>&nbsp;An auto review will be launched at the deadline</li>
    </ul>
</div>
<div>
    <h4>In a nutshell&hellip;</h4>
    <ul>
        <li><strong>Auto QA review:</strong> 0.0/8 mandatory &amp; 0.0/1 optional</li>
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
            <li><a href="https://intranet.alxswe.com/concepts/12">DNS</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/68">Web stack debugging</a></li>
        </ul>
    </div>
</div>
<div>
    <div>
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/FlhGPEK.png" alt=""></p>
        <h2>Background Context</h2>
        <h3>What happens when you don&rsquo;t secure your website traffic?</h3>
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/xCmOCgw.gif" alt=""></p>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/XT1BAiBL3Jpq1bn1q6IYXQ" title="What is HTTPS?" target="_blank">What is HTTPS?</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/STj5WkAPACBxOvwB77Ycrw" title="What are the 2 main elements that SSL is providing" target="_blank">What are the 2 main elements that SSL is providing</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/mJNlqZkTBxIxM2bpDK_VoA" title="HAProxy SSL termination on Ubuntu16.04" target="_blank">HAProxy SSL termination on Ubuntu16.04</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/CKUICfppIWI6UC0coEMB8g" title="SSL termination" target="_blank">SSL termination</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/zPjZ7-eSSQsLFsGA16C1HQ" title="Bash function" target="_blank">Bash function</a></li>
        </ul>
        <p><strong>man or help</strong>:</p>
        <ul>
            <li><code>awk</code></li>
            <li><code>dig</code></li>
        </ul>
        <h2>Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/fJ20wsMngb_yNAhGgBwzlQ" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
        <h3>General</h3>
        <ul>
            <li>What is HTTPS SSL 2 main roles</li>
            <li>What is the purpose encrypting traffic</li>
            <li>What SSL termination means</li>
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
<div>
    <div>
        <h3>Quiz questions</h3>
    </div>
    <div>
        <div><strong>Great!</strong> You&apos;ve completed the quiz successfully! Keep going!&nbsp;(Show quiz)</div>
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
            <h3>0. World wide web</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Configure your domain zone so that the subdomain&nbsp;<code>www</code> points to your load-balancer IP (<code>lb-01</code>). Let&rsquo;s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.</p>
            <p>Requirements:</p>
            <ul>
                <li>Add the subdomain&nbsp;<code>www</code> to your domain, point it to your&nbsp;<code>lb-01</code> IP (your domain name might be configured with default subdomains, feel free to remove them)</li>
                <li>Add the subdomain&nbsp;<code>lb-01</code> to your domain, point it to your&nbsp;<code>lb-01</code> IP</li>
                <li>Add the subdomain&nbsp;<code>web-01</code> to your domain, point it to your&nbsp;<code>web-01</code> IP</li>
                <li>Add the subdomain&nbsp;<code>web-02</code> to your domain, point it to your&nbsp;<code>web-02</code> IP</li>
                <li>Your Bash script must accept 2 arguments:<ol>
                        <li><code>domain</code>:<ul>
                                <li>type: string</li>
                                <li>what: domain name to audit</li>
                                <li>mandatory: yes</li>
                            </ul>
                        </li>
                        <li><code>subdomain</code>:<ul>
                                <li>type: string</li>
                                <li>what: specific subdomain to audit</li>
                                <li>mandatory: no</li>
                            </ul>
                        </li>
                    </ol>
                </li>
                <li>Output:&nbsp;<code>The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]</code></li>
                <li>When only the parameter&nbsp;<code>domain</code> is provided, display information for its subdomains&nbsp;<code>www</code>,&nbsp;<code>lb-01</code>,&nbsp;<code>web-01</code> and&nbsp;<code>web-02</code> - in this specific order</li>
                <li>When passing&nbsp;<code>domain</code> and&nbsp;<code>subdomain</code> parameters, display information for the specified subdomain</li>
                <li>Ignore&nbsp;<code>shellcheck</code> case&nbsp;<code>SC2086</code></li>
                <li>Must use:<ul>
                        <li><code>awk</code></li>
                        <li>at least one Bash function</li>
                    </ul>
                </li>
                <li>You do not need to handle edge cases such as:<ul>
                        <li>Empty parameters</li>
                        <li>Nonexistent domain names</li>
                        <li>Nonexistent subdomains</li>
                    </ul>
                </li>
            </ul>
            <p>Example:</p>
            <pre><code>sylvain@ubuntu$ dig www.holberton.online | grep -A1 &apos;ANSWER SECTION:&apos;
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 &apos;ANSWER SECTION:&apos;
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 &apos;ANSWER SECTION:&apos;
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 &apos;ANSWER SECTION:&apos;
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x10-https_ssl</code></li>
                    <li>File:&nbsp;<code>0-world_wide_web</code></li>
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
            <h3>1. HAproxy SSL termination</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>&ldquo;Terminating SSL on HAproxy&rdquo; means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.</p>
            <p>Create a certificate using&nbsp;<code>certbot</code> and configure&nbsp;<code>HAproxy</code> to accept encrypted traffic for your subdomain&nbsp;<code>www.</code>.</p>
            <p>Requirements:</p>
            <ul>
                <li>HAproxy must be listening on port TCP 443</li>
                <li>HAproxy must be accepting SSL traffic</li>
                <li>HAproxy must serve encrypted traffic that will return the&nbsp;<code>/</code> of your web server</li>
                <li>When querying the root of your domain name, the page returned must contain&nbsp;<code>Holberton School</code></li>
                <li>Share your HAproxy config as an answer file (<code>/etc/haproxy/haproxy.cfg</code>)</li>
            </ul>
            <p>The file&nbsp;<code>1-haproxy_ssl_termination</code> must be your HAproxy configuration file</p>
            <p>Make sure to install HAproxy 1.5 or higher,&nbsp;<a href="https://intranet.alxswe.com/rltoken/CKUICfppIWI6UC0coEMB8g" title="SSL termination" target="_blank">SSL termination</a> is not available before v1.5.</p>
            <p>Example:</p>
            <pre><code>sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: &quot;58abea7c-1e&quot;
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x10-https_ssl</code></li>
                    <li>File:&nbsp;<code>1-haproxy_ssl_termination</code></li>
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
            <h3>2. No loophole in your website traffic</h3>
            <div>#advanced</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.</p>
            <p>Requirements:</p>
            <ul>
                <li>This should be transparent to the user</li>
                <li>HAproxy should return a&nbsp;<a href="https://intranet.alxswe.com/rltoken/yGdTSvZAzHMnDEhalTjNUw" title="301" target="_blank">301</a></li>
                <li>HAproxy should redirect HTTP traffic to HTTPS</li>
                <li>Share your HAproxy config as an answer file (<code>/etc/haproxy/haproxy.cfg</code>)</li>
            </ul>
            <p>The file&nbsp;<code>100-redirect_http_to_https</code> must be your HAproxy configuration file</p>
            <p>Example:</p>
            <pre><code>sylvain@ubuntu$ curl -sIL http://www.holberton.online
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://www.holberton.online/
Connection: close

HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 02:19:18 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: &quot;58abea7c-1e&quot;
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x10-https_ssl</code></li>
                    <li>File:&nbsp;<code>100-redirect_http_to_https</code></li>
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
