<main>
    <article>
        <div>
            <div>
                <h1>0x08. Networking basics #1</h1>
                <div>
                    <div>DevOpsNetworkSysAdmin</div>
                </div>
                <div>
                    <ul>
                        <li>&nbsp;By: Sylvain Kalache</li>
                        <li>&nbsp;Weight: 1</li>
                        <li>&nbsp;Project over - took place from <span title="">May 4, 2023 6:00 AM</span> to <span title="">May 5, 2023 6:00 AM</span></li>
                        <li>&nbsp;An auto review will be launched at the deadline</li>
                    </ul>
                </div>
                <div>
                    <h4>In a nutshell&hellip;</h4>
                    <ul>
                        <li><strong>Auto QA review:</strong> 0.0/3 mandatory &amp; 0.0/1 optional</li>
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
                        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/285/s7kpNYq.png" alt=""></p>
                        <h2>Resources</h2>
                        <p><strong>Read or watch</strong>:</p>
                        <ul>
                            <li><a href="https://intranet.alxswe.com/rltoken/Odcc_tyAQlcANCCrtmxo6A" title="What is localhost" target="_blank">What is localhost</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/fUb9IpnxrNaddMljzwbhJQ" title="What is 0.0.0.0" target="_blank">What is 0.0.0.0</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/4_MBpFTulKliFM69jCPzOQ" title="What is the hosts file" target="_blank">What is the hosts file</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/OR0lOEwAw9I1Rj4aGp1Ljg" title="Netcat examples" target="_blank">Netcat examples</a></li>
                        </ul>
                        <p><strong>man or help</strong>:</p>
                        <ul>
                            <li><code>ifconfig</code></li>
                            <li><code>telnet</code></li>
                            <li><code>nc</code></li>
                            <li><code>cut</code></li>
                        </ul>
                        <h2>Learning Objectives</h2>
                        <p>At the end of this project, you are expected to be able to <a href="https://intranet.alxswe.com/rltoken/IpTKeVwlKHT4ZVva_T891w" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
                        <h3>General</h3>
                        <ul>
                            <li>What is localhost/127.0.0.1</li>
                            <li>What is 0.0.0.0</li>
                            <li>What is <code>/etc/hosts</code></li>
                            <li>How to display your machine&rsquo;s active network interfaces</li>
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
                            <li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
                            <li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
                            <li>All your files should end with a new line</li>
                            <li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
                            <li>All your Bash script files must be executable</li>
                            <li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.7.0</code> via <code>apt-get</code>) without any errors</li>
                            <li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
                            <li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
                        </ul>
                    </div>
                </div>
                <div>
                    <div>
                        <h3>Quiz questions</h3>
                    </div>
                    <div>
                        <div><strong>Great!</strong> You&apos;ve completed the quiz successfully! Keep going! (Show quiz)</div>
                    </div>
                </div>
                <h2>Tasks</h2>
                <div>
                    <div>
                        <div>
                            <h3>0. Change your home IP</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p>Write a Bash script that configures an Ubuntu server with the below requirements.</p>
                            <p>Requirements:</p>
                            <ul>
                                <li><code>localhost</code> resolves to <code>127.0.0.2</code></li>
                                <li><code>facebook.com</code> resolves to <code>8.8.8.8</code>.</li>
                                <li>The checker is running on Docker, so make sure to read <a href="https://intranet.alxswe.com/rltoken/XSXhQPoDu3QecXs3j9XgPQ" title="this" target="_blank">this</a></li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>sylvain@ubuntu$ ping localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.012 ms
^C
--- localhost ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.012/0.012/0.012/0.000 ms
sylvain@ubuntu$
sylvain@ubuntu$ ping facebook.com
PING facebook.com (157.240.11.35) 56(84) bytes of data.
64 bytes from edge-star-mini-shv-02-lax3.facebook.com (157.240.11.35): icmp_seq=1 ttl=63 time=15.4 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 15.432/15.432/15.432/0.000 ms
sylvain@ubuntu$
sylvain@ubuntu$ sudo ./0-change_your_home_IP
sylvain@ubuntu$
sylvain@ubuntu$ ping localhost
PING localhost (127.0.0.2) 56(84) bytes of data.
64 bytes from localhost (127.0.0.2): icmp_seq=1 ttl=64 time=0.012 ms
64 bytes from localhost (127.0.0.2): icmp_seq=2 ttl=64 time=0.036 ms
^C
--- localhost ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.012/0.024/0.036/0.012 ms
sylvain@ubuntu$
sylvain@ubuntu$ ping facebook.com
PING facebook.com (8.8.8.8) 56(84) bytes of data.
64 bytes from facebook.com (8.8.8.8): icmp_seq=1 ttl=63 time=8.06 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 8.065/8.065/8.065/0.000 ms
</code></pre>
                            <p>In this example we can see that:</p>
                            <ul>
                                <li>before running the script, <code>localhost</code> resolves to <code>127.0.0.1</code> and <code>facebook.com</code> resolves to <code>157.240.11.35</code></li>
                                <li>after running the script, <code>localhost</code> resolves to <code>127.0.0.2</code> and <code>facebook.com</code> resolves to <code>8.8.8.8</code></li>
                            </ul>
                            <p>If you&rsquo;re running this script on a machine that you&rsquo;ll continue to use, be sure to revert <code>localhost</code> to <code>127.0.0.1</code>. Otherwise, a lot of things will stop working!</p>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
                                    <li>Directory: <code>0x08-networking_basics_2</code></li>
                                    <li>File: <code>0-change_your_home_IP</code></li>
                                </ul>
                            </div>
                        </div>
                        <div>
                            <div>
                                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Ask for a new correction</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                                <div><br></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <div>
                        <div>
                            <h3>1. Show attached IPs</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p>Write a Bash script that displays all active IPv4 IPs on the machine it&rsquo;s executed on.</p>
                            <p>Example:</p>
                            <pre><code>sylvain@ubuntu$ ./1-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
sylvain@ubuntu$
</code></pre>
                            <p>Obviously, the IPs displayed may be different depending on which machine you are running the script on.</p>
                            <p>Note that we can see our <code>localhost</code> IP :)</p>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
                                    <li>Directory: <code>0x08-networking_basics_2</code></li>
                                    <li>File: <code>1-show_attached_IPs</code></li>
                                </ul>
                            </div>
                        </div>
                        <div>
                            <div>
                                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Ask for a new correction</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                                <div><br></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <div>
                        <div>
                            <h3>2. Port listening on localhost</h3>
                            <div>#advanced</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p>Write a Bash script that listens on port <code>98</code> on <code>localhost</code>.</p>
                            <p><strong>Terminal 0</strong></p>
                            <p>Starting my script.</p>
                            <pre><code>sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
</code></pre>
                            <p><strong>Terminal 1</strong></p>
                            <p>Connecting to <code>localhost</code> on port <code>98</code> using <code>telnet</code> and typing some text.</p>
                            <pre><code>sylvain@ubuntu$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is &apos;^]&apos;.
Hello world
test
</code></pre>
                            <p><strong>Terminal 0</strong></p>
                            <p>Receiving the text on the other side.</p>
                            <pre><code>sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
Hello world
test
</code></pre>
                            <p>For the sake of the exercise, this connection is made entirely within <code>localhost</code>. This isn&rsquo;t really exciting as is, but we can use this script across networks as well. Try running it between your local PC and your remote server for fun!</p>
                            <p>As you can see, this can come in very handy in a multitude of situations. Maybe you&rsquo;re debugging socket connection issues, or you&rsquo;re trying to connect to a software and you are unsure if the issue is the software or the network, or you&rsquo;re working on firewall rules&hellip; Another tool to add to your debugging toolbox!</p>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
                                    <li>Directory: <code>0x08-networking_basics_2</code></li>
                                    <li>File: <code>100-port_listening_on_localhost</code></li>
                                </ul>
                            </div>
                        </div>
                        <div>
                            <div>
                                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Ask for a new correction</button> <button>Get a sandbox</button>&nbsp;</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </article>
</main>