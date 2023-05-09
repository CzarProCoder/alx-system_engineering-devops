<h1>0x07. Networking basics #0</h1>
<div>
    <div>DevOpsNetwork</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Sylvain Kalache</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Project over - took place from&nbsp;<span title="">May 4, 2023 6:00 AM</span> to&nbsp;<span title="">May 5, 2023 6:00 AM</span></li>
        <li>&nbsp;An auto review will be launched at the deadline</li>
    </ul>
</div>
<div>
    <h4>In a nutshell&hellip;</h4>
    <ul>
        <li><strong>Auto QA review:</strong> 0.0/13 mandatory</li>
        <li><strong>Altogether:</strong>&nbsp; <strong>0.0%</strong>
            <ul>
                <li>Mandatory: 0.0%</li>
                <li>Optional: no optional tasks</li>
            </ul>
        </li>
    </ul>
</div>
<div>
    <div>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/k2uCsynicuNbu1cAQhXqVQ" title="OSI model" target="_blank">OSI model</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/XW3ZGm5Ya_a8XVDXcAKT_A" title="Different types of network" target="_blank">Different types of network</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/en370-Hrwgi_GUvFcg3bKg" title="LAN network" target="_blank">LAN network</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/Ah1EKqnINR85lM4P2WnLSw" title="WAN network" target="_blank">WAN network</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/Lwh9xQxFD4dWh5sIApXI1g" title="Internet" target="_blank">Internet</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/j-Wp-YRvFTVP04SpIeRzHQ" title="MAC address" target="_blank">MAC address</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/HaZZvrmGaQ3U7ZLDYgZb6w" title="What is an IP address" target="_blank">What is an IP address</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/OPJCZYuWSEXLIZOqU9Uc0A" title="Private and public address" target="_blank">Private and public address</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/M8g-egWLlldTl6Y0QECdwA" title="IPv4 and IPv6" target="_blank">IPv4 and IPv6</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/7lj-zoZQ7xFTkj4MTyos_g" title="Localhost" target="_blank">Localhost</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/uJbs8E9-FyATfsELpmtTIg" title="TCP and UDP" target="_blank">TCP and UDP</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/4PYkqDfOvIZZb9aUPGOOzQ" title="TCP/UDP ports List" target="_blank">TCP/UDP ports List</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/3zBgO6r2M1Q8lUVt9g8aJw" title="What is ping /ICMP" target="_blank">What is ping /ICMP</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/ZbMHH3jmxFhcrbigVy15iw" title="Positional parameters" target="_blank">Positional parameters</a></li>
        </ul>
        <p><strong>man or help</strong>:</p>
        <ul>
            <li><code>netstat</code></li>
            <li><code>ping</code></li>
        </ul>
        <h2>Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/RowLuXQWMOPFHaboo_3odA" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
        <h3>OSI Model</h3>
        <ul>
            <li>What it is</li>
            <li>How many layers it has</li>
            <li>How it is organized</li>
        </ul>
        <h3>What is a LAN</h3>
        <ul>
            <li>Typical usage</li>
            <li>Typical geographical size</li>
        </ul>
        <h3>What is a WAN</h3>
        <ul>
            <li>Typical usage</li>
            <li>Typical geographical size</li>
        </ul>
        <h3>What is the Internet</h3>
        <ul>
            <li>What is an IP address</li>
            <li>What are the 2 types of IP address</li>
            <li>What is&nbsp;<code>localhost</code></li>
            <li>What is a subnet</li>
            <li>Why IPv6 was created</li>
        </ul>
        <h3>TCP/UDP</h3>
        <ul>
            <li>What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)</li>
            <li>What is the main difference between TCP and UDP</li>
            <li>What is a port</li>
            <li>Memorize SSH, HTTP and HTTPS port numbers</li>
            <li>What tool/protocol is often used to check if a device is connected to a network</li>
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
            <li>All your Bash script files will be interpreted on Ubuntu 20.04 LTS</li>
            <li>All your files should end with a new line</li>
            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>All your Bash script files must be executable</li>
            <li>Your Bash script must pass&nbsp;<code>shellcheck</code> without any error</li>
            <li>The first line of all your Bash scripts should be exactly&nbsp;<code>#!/usr/bin/env bash</code></li>
            <li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
        </ul>
        <h2>More Info</h2>
        <p>The second line of all your Bash scripts should be a comment explaining what is the script doing</p>
        <p>For multiple choice question type tasks, just type the number of the correct answer in your answer file, add a new line for every new answer, example:</p>
        <p>What is the most important position in a software company?</p>
        <ol>
            <li>Project manager</li>
            <li>Backend developer</li>
            <li>System administrator</li>
        </ol>
        <pre><code>sylvain@ubuntu$ cat foo_answer_file
3
sylvain@ubuntu$
</code></pre>
        <p>Source for question 1&nbsp;<a href="https://intranet.alxswe.com/rltoken/iEZZ6SemL1HJHjaJOjlPYQ" title="here" target="_blank">here</a></p>
    </div>
</div>
<h2>Tasks</h2>
<div>
    <div>
        <div>
            <h3>0. OSI model</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.</p>
            <p>It is organized from the lowest level to the highest level:</p>
            <ul>
                <li>The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal</li>
                <li>The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc</li>
            </ul>
            <p>Keep in mind that the OSI model is a concept, it&rsquo;s not even tangible. The OSI model doesn&rsquo;t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communications systems.</p>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/4e6a0ad87a65d7054248.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230509%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230509T082118Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c234e70240e4b33ffac51fb41a3f0cb92427c83ea5c03d019e440aff707eed39" alt=""></p>
            <p>In this project we will mainly focus on:</p>
            <ul>
                <li>The Transport layer and especially TCP/UDP</li>
                <li>On the Network layer with IP and ICMP</li>
            </ul>
            <p>The image bellow describes more concretely how you can relate to every level.</p>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/0fc96bd99faa7941b18bcae4c5f90c6acd11791d.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230509%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230509T082118Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ab4a6e22a05ac66ec76766f05f319f8e6c3bb7334535c5bdf4818b19902756b1" alt=""></p>
            <p>Questions:</p>
            <p>What is the OSI model?</p>
            <ol>
                <li>Set of specifications that network hardware manufacturers must respect</li>
                <li>The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology</li>
                <li>The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology</li>
            </ol>
            <p>How is the OSI model organized?</p>
            <ol>
                <li>Alphabetically</li>
                <li>From the lowest to the highest level</li>
                <li>Randomly</li>
            </ol>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x07-networking_basics</code></li>
                    <li>File:&nbsp;<code>0-OSI_model</code></li>
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
            <h3>1. Types of network</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/4b995d4f8078b44afa968d68a98035d2bd7e8fac.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230509%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230509T082118Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1fd289f5db135ad7abdc2ff216066d3811679a6669cd45122806b9f65e51c0a8" alt=""></p>
            <p>LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.</p>
            <p>Questions:</p>
            <p>What type of network a computer in local is connected to?</p>
            <ol>
                <li>Internet</li>
                <li>WAN</li>
                <li>LAN</li>
            </ol>
            <p>What type of network could connect an office in one building to another office in a building a few streets away?</p>
            <ol>
                <li>Internet</li>
                <li>WAN</li>
                <li>LAN</li>
            </ol>
            <p>What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?</p>
            <ol>
                <li>Internet</li>
                <li>WAN</li>
                <li>LAN</li>
            </ol>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x07-networking_basics</code></li>
                    <li>File:&nbsp;<code>1-types_of_network</code></li>
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
            <h3>2. MAC and IP address</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/1e348ba3bcbb094b02922f821ffeb3d8c5438b7b.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230509%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230509T082119Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=85d23d84d03c2e525a243870da16f03c9881b31db724f62c5d1f886e7578e1c0" alt=""></p>
            <p>Questions:</p>
            <p>What is a MAC address?</p>
            <ol>
                <li>The name of a network interface</li>
                <li>The unique identifier of a network interface</li>
                <li>A network interface</li>
            </ol>
            <p>What is an IP address?</p>
            <ol>
                <li>Is to devices connected to a network what postal address is to houses</li>
                <li>The unique identifier of a network interface</li>
                <li>Is a number that network devices use to connect to networks</li>
            </ol>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x07-networking_basics</code></li>
                    <li>File:&nbsp;<code>2-MAC_and_IP_address</code></li>
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
            <h3>3. UDP and TCP</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/3d92e3c4a470f8ecf4c73db511fcbbadaa002e1c.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230509%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230509T082119Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=eda50ca37b719fad6fd3826ecea40e492ebf04351f8506a71096da1a1f93aee4" alt=""></p>
            <p>Let&rsquo;s fill the empty parts in the drawing above.</p>
            <p>Questions:</p>
            <ul>
                <li>Which statement is correct for the TCP box:<ol>
                        <li><code>It is a protocol that is transferring data in a slow way but surely</code></li>
                        <li><code>It is a protocol that is transferring data in a fast way and might loss data along in the process</code></li>
                    </ol>
                </li>
                <li>Which statement is correct for the UDP box:<ol>
                        <li><code>It is a protocol that is transferring data in a slow way but surely</code></li>
                        <li><code>It is a protocol that is transferring data in a fast way and might loss data along in the process</code></li>
                    </ol>
                </li>
                <li>Which statement is correct for the TCP worker:<ol>
                        <li><code>Have you received boxes x, y, z?</code></li>
                        <li><code>May I increase the rate at which I am sending you boxes?</code></li>
                    </ol>
                </li>
            </ul>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x07-networking_basics</code></li>
                    <li>File:&nbsp;<code>3-UDP_and_TCP</code></li>
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
            <h3>4. TCP and UDP ports</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.</p>
            <p>If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.</p>
            <p>While the full list of ports should not be memorized, it is important to know the most used ports, let&rsquo;s start by remembering 3 of them:</p>
            <ul>
                <li><strong>22</strong> for SSH</li>
                <li><strong>80</strong> for HTTP</li>
                <li><strong>443</strong> for HTTPS</li>
            </ul>
            <p>Note that a specific&nbsp;<a href="https://intranet.alxswe.com/rltoken/tMKODilbDVpB8EgfIRDJVw" title="IP + port = socket" target="_blank">IP + port = socket</a>.</p>
            <p>Write a Bash script that displays listening ports:</p>
            <ul>
                <li>That only shows listening sockets</li>
                <li>That shows the PID and name of the program to which each socket belongs</li>
            </ul>
            <p>Example:</p>
            <pre><code>sylvain@ubuntu$ sudo ./4-TCP_and_UDP_ports
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 *:sunrpc                *:*                     LISTEN      518/rpcbind
tcp        0      0 *:ssh                   *:*                     LISTEN      1240/sshd
tcp        0      0 *:32938                 *:*                     LISTEN      547/rpc.statd
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN      518/rpcbind
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      1240/sshd
tcp6       0      0 [::]:33737              [::]:*                  LISTEN      547/rpc.statd
udp        0      0 *:sunrpc                *:*                                 518/rpcbind
udp        0      0 *:691                   *:*                                 518/rpcbind
udp        0      0 localhost:723           *:*                                 547/rpc.statd
udp        0      0 *:60129                 *:*                                 547/rpc.statd
udp        0      0 *:3845                  *:*                                 562/dhclient
udp        0      0 *:bootpc                *:*                                 562/dhclient
udp6       0      0 [::]:47444              [::]:*                              547/rpc.statd
udp6       0      0 [::]:sunrpc             [::]:*                              518/rpcbind
udp6       0      0 [::]:50038              [::]:*                              562/dhclient
udp6       0      0 [::]:691                [::]:*                              518/rpcbind
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ACC ]     STREAM     LISTENING     7724     518/rpcbind         /run/rpcbind.sock
unix  2      [ ACC ]     STREAM     LISTENING     6525     1/init              @/com/ubuntu/upstart
unix  2      [ ACC ]     STREAM     LISTENING     8559     835/dbus-daemon     /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     9190     1087/acpid          /var/run/acpid.socket
unix  2      [ ACC ]     SEQPACKET  LISTENING     7156     378/systemd-udevd   /run/udev/control
sylvain@ubuntu$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x07-networking_basics</code></li>
                    <li>File:&nbsp;<code>4-TCP_and_UDP_ports</code></li>
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
            <h3>5. Is the host on the network</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p><img src="https://media.giphy.com/media/uDxkJAVSU7GY8/giphy.gif" alt=""></p>
            <p>The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command&nbsp;<code>ping</code> uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.</p>
            <p>Write a Bash script that pings an IP address passed as an argument.</p>
            <p>Requirements:</p>
            <ul>
                <li>Accepts a string as an argument</li>
                <li>Displays&nbsp;<code>Usage: 5-is_the_host_on_the_network {IP_ADDRESS}</code> if no argument passed</li>
                <li>Ping the IP 5 times</li>
            </ul>
            <p>Example:</p>
            <pre><code>sylvain@ubuntu$ ./5-is_the_host_on_the_network 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=12.9 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=13.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=7.83 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=63 time=11.3 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=63 time=7.57 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 7.570/10.682/13.679/2.546 ms
sylvain@ubuntu$
sylvain@ubuntu$ ./5-is_the_host_on_the_network
Usage: 5-is_the_host_on_the_network {IP_ADDRESS}
sylvain@ubuntu$ 
</code></pre>
            <p>It is interesting to look at the&nbsp;<code>time</code> value, which is the time that it took for the ICMP request to go to the&nbsp;<code>8.8.8.8</code> IP and come back to my host. The IP&nbsp;<code>8.8.8.8</code> is owned by Google, and the quickest roundtrip between my computer and Google was 7.57 ms which is pretty fast, which is a sign that the network path between my computer and Google&rsquo;s datacenter is in good shape. A slow ping would indicate a slow network.</p>
            <p>Next time you feel that your connection is slow, try the&nbsp;<code>ping</code> command to see what is going on!</p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x07-networking_basics</code></li>
                    <li>File:&nbsp;<code>5-is_the_host_on_the_network</code></li>
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