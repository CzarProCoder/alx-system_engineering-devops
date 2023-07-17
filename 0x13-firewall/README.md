<h1>0x13. Firewall</h1>
<div>
    <div>DevOpsSysAdminSecurity</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Sylvain Kalache, co-founder at Holberton School</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Project will start&nbsp;<span title="">Jul 17, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Jul 18, 2023 6:00 AM</span></li>
        <li>&nbsp;Checker&nbsp;was&nbsp;released at&nbsp;<span title="">Jul 17, 2023 12:00 PM</span></li>
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
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png" alt=""></p>
        <h2>Background Context</h2>
        <h3>Your servers without a firewall&hellip;</h3>
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif" alt=""></p>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/vjB4LyHRdtEImzZcuD89ZQ" title="What is a firewall" target="_blank">What is a firewall</a></li>
        </ul>
        <h2>More Info</h2>
        <p>As explained in the&nbsp;<strong>web stack debugging guide</strong> concept page,&nbsp;<code>telnet</code> is a very good tool to check if sockets are open with&nbsp;<code>telnet IP PORT</code>. For example, if you want to check if port 22 is open on&nbsp;<code>web-02</code>:</p>
        <pre><code>sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is &apos;^]&apos;.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$
</code></pre>
        <p>We can see for this example that the connection is successful:&nbsp;<code>Connected to web-02.holberton.online.</code></p>
        <p>Now let&rsquo;s try connecting to port 2222:</p>
        <pre><code>sylvain@ubuntu$ telnet web-02.holberton.online 2222
Trying 54.89.38.100...
^C
sylvain@ubuntu$
</code></pre>
        <p>We can see that the connection never succeeds, so after some time I just use&nbsp;<code>ctrl+c</code> to kill the process.</p>
        <p>This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.</p>
        <p>Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on&nbsp;<code>web-01</code>, please perform the test from outside of the school network, like from your&nbsp;<code>web-02</code> server. If you SSH into your&nbsp;<code>web-02</code> server, the traffic will be originating from&nbsp;<code>web-02</code> and not from the school&rsquo;s network, bypassing the firewall.</p>
        <h2>Warning!</h2>
        <p><strong>Containers on demand cannot be used for this project (Docker container limitation)</strong></p>
        <p><strong>Be very careful with firewall rules! For instance, if you ever deny port&nbsp;<code>22/TCP</code> and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.</strong></p>
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
            <h3>0. Block all incoming traffic but</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Let&rsquo;s install the&nbsp;<code>ufw</code> firewall and setup a few rules on&nbsp;<code>web-01</code>.</p>
            <p>Requirements:</p>
            <ul>
                <li>The requirements below must be applied to&nbsp;<code>web-01</code> (feel free to do it on&nbsp;<code>lb-01</code> and&nbsp;<code>web-02</code>, but it won&rsquo;t be checked)</li>
                <li>Configure&nbsp;<code>ufw</code> so that it blocks all incoming traffic, except the following TCP ports:<ul>
                        <li><code>22</code> (SSH)</li>
                        <li><code>443</code> (HTTPS SSL)</li>
                        <li><code>80</code> (HTTP)</li>
                    </ul>
                </li>
                <li>Share the&nbsp;<code>ufw</code> commands that you used in your answer file</li>
            </ul>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x13-firewall</code></li>
                    <li>File:&nbsp;<code>0-block_all_incoming_traffic_but</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>1. Port forwarding</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Firewalls can not only filter requests, they can also forward them.</p>
            <p>Requirements:</p>
            <ul>
                <li>Configure&nbsp;<code>web-01</code> so that its firewall redirects port&nbsp;<code>8080/TCP</code> to port&nbsp;<code>80/TCP</code>.</li>
                <li>Your answer file should be a copy of the&nbsp;<code>ufw</code> configuration file that you modified to make this happen</li>
            </ul>
            <p>Terminal in&nbsp;<code>web-01</code>:</p>
            <pre><code>root@03-web-01:~# netstat -lpn
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      2473/nginx
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      978/sshd
tcp6       0      0 :::80                   :::*                    LISTEN      2473/nginx
tcp6       0      0 :::22                   :::*                    LISTEN      978/sshd
udp        0      0 0.0.0.0:68              0.0.0.0:*                           594/dhclient
udp        0      0 0.0.0.0:54432           0.0.0.0:*                           594/dhclient
udp6       0      0 :::32563                :::*                                594/dhclient
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ACC ]     SEQPACKET  LISTENING     7175     433/systemd-udevd   /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     6505     1/init              @/com/ubuntu/upstart
unix  2      [ ACC ]     STREAM     LISTENING     8048     741/dbus-daemon     /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     8419     987/acpid           /var/run/acpid.socket
root@03-web-01:~#
root@03-web-01:~# grep listen /etc/nginx/sites-enabled/default
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;
    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
#   listen 8000;
#   listen somename:8080;
#   listen 443;
root@03-web-01:~#
</code></pre>
            <ul>
                <li>My web server&nbsp;<code>nginx</code> is only listening on port&nbsp;<code>80</code></li>
                <li><code>netstat</code> shows that nothing is listening on&nbsp;<code>8080</code></li>
            </ul>
            <p>Terminal in&nbsp;<code>web-02</code>:</p>
            <pre><code>ubuntu@03-web-02:~$ curl -sI web-01.holberton.online:80
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 07 Mar 2017 02:14:41 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: &quot;5315bd25-264&quot;
Accept-Ranges: bytes

ubuntu@03-web-02:~$ curl -sI web-01.holberton.online:8080
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 07 Mar 2017 02:14:43 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: &quot;5315bd25-264&quot;
Accept-Ranges: bytes

ubuntu@03-web-02:~$
</code></pre>
            <p>I use curl to query&nbsp;<code>web-01.holberton.online</code>, and since my firewall is forwarding the ports, I get a&nbsp;<code>HTTP 200</code> response on port&nbsp;<code>80/TCP</code> and also on port&nbsp;<code>8080/TCP</code>.</p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x13-firewall</code></li>
                    <li>File:&nbsp;<code>100-port_forwarding</code></li>
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
