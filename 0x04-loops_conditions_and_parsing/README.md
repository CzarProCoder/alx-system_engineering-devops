<h1>0x04. Loops, conditions and parsing</h1>
<div>
    <div>DevOpsShellBashScripting</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Sylvain Kalache</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Ongoing second chance project - started&nbsp;<span title="">Apr 27, 2023 6:00 AM</span>, must end by&nbsp;<span title="">May 3, 2023 6:00 AM</span></li>
        <li>&nbsp;An auto review will be launched at the deadline</li>
    </ul>
</div>
<div>
    <h4>In a nutshell&hellip;</h4>
    <ul>
        <li><strong>Auto QA review:</strong> 0.0/83 mandatory &amp; 0.0/30 optional</li>
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
    <h2>About&nbsp;Bash&nbsp;projects</h2>
    <p><br></p>
    <p>Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.</p>
    <p><br></p>
</div>
<div>
    <div>
        <h2>Background Context</h2>
        <p><a href="https://youtu.be/BC2neyc5GcI" target="_blank"><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/b07e3333b1edfb9beed5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230501%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230501T150637Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f7d294a20ebb4c18f1e854ffe8f958bab02aefa13db0620fca69803e42ac7e48" alt=""></a></p>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/wT98UJfv_E2tk4yP9PcLLw" title='The <code>for</code> loop" target=“_blank”>The <code>for</code> loop</a> </li><li><a href=' target="_blank">Loops sample</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/olvOKX699pq50rkHRE5cSA" title="Variable assignment and arithmetic" target="_blank">Variable assignment and arithmetic</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/HxohzllkOWh0t4dy_HptIQ" title="Comparison operators" target="_blank">Comparison operators</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/g8of2ABPEJfCNtPrDQaqVw" title="File test operators" target="_blank">File test operators</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/O0Ay21p7tDhfLMsYbtAKug" title="Make your scripts portable" target="_blank">Make your scripts portable</a></li>
        </ul>
        <p><strong>man or help</strong>:</p>
        <ul>
            <li><code>env</code></li>
            <li><code>cut</code></li>
            <li><code>for</code></li>
            <li><code>while</code></li>
            <li><code>until</code></li>
            <li><code>if</code></li>
        </ul>
        <h2>Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/UnkzDNdH09TFJ0-Y56azyg" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
        <h3>General</h3>
        <ul>
            <li>How to create SSH keys</li>
            <li>What is the advantage of using&nbsp;<code>#!/usr/bin/env bash</code> over&nbsp;<code>#!/bin/bash</code></li>
            <li>How to use&nbsp;<code>while</code>,&nbsp;<code>until</code> and&nbsp;<code>for</code> loops</li>
            <li>How to use&nbsp;<code>if</code>,&nbsp;<code>else</code>,&nbsp;<code>elif</code> and&nbsp;<code>case</code> condition statements</li>
            <li>How to use the&nbsp;<code>cut</code> command</li>
            <li>What are files and other comparison operators, and how to use them</li>
        </ul>
        <h2>Requirements</h2>
        <h3>General</h3>
        <ul>
            <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
            <li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
            <li>All your files should end with a new line</li>
            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>All your Bash script files must be executable</li>
            <li>You are not allowed to use&nbsp;<code>awk</code></li>
            <li>Your Bash script must pass&nbsp;<code>Shellcheck</code> (version&nbsp;<code>0.7.0</code>) without any error</li>
            <li>The first line of all your Bash scripts should be exactly&nbsp;<code>#!/usr/bin/env bash</code></li>
            <li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
        </ul>
        <h3>Copyright - Plagiarism</h3>
        <ul>
            <li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
            <li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else&rsquo;s work.</li>
            <li>You are not allowed to publish any content of this project.</li>
            <li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
        </ul>
        <h2>More Info</h2>
        <h3>Shellcheck</h3>
        <p><a href="https://intranet.alxswe.com/rltoken/joK6l_yEZ9N7T0GQ1RDjLA" title="Shellcheck" target="_blank">Shellcheck</a> is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about.&nbsp;<code>Shellcheck</code> is your friend!&nbsp;<strong>All your Bash scripts must pass&nbsp;<code>Shellcheck</code> without any error or you will not get any points on the task</strong>.</p>
        <p><code>Shellcheck</code> is available on the school&rsquo;s computers. If you want to use it on your own computer, here is how to&nbsp;<a href="https://intranet.alxswe.com/rltoken/jbz0_-i3TV3WpKgxhyrtpA" title="install it" target="_blank">install it</a>.</p>
        <p>Examples:</p>
        <p>Not passing&nbsp;<code>Shellcheck</code>:<br><br><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png" alt=""></p>
        <p>Passing&nbsp;<code>Shellcheck</code>:<br><br><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png" alt=""></p>
        <p>For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code&nbsp;<code>SC2034</code>, you can browse&nbsp;<a href="https://intranet.alxswe.com/rltoken/dxp49_rfO4_9Yjtcg59exg" title="https://github.com/koalaman/shellcheck/wiki/SC2034" target="_blank">https://github.com/koalaman/shellcheck/wiki/SC2034</a>.</p>
    </div>
</div>
<h2>Tasks</h2>
<div>
    <div>
        <div>
            <h3>0. Create a SSH RSA key pair</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Read for this task:</p>
            <ul>
                <li><a href="https://intranet.alxswe.com/rltoken/Cy1plV2eR3VphjPqliXB8A" title="Linux and Mac OS users" target="_blank">Linux and Mac OS users</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/PXriGT0IKaSXC7L5l0CVag" title="Windows users" target="_blank">Windows users</a></li>
            </ul>
            <p>man:&nbsp;<code>ssh-keygen</code></p>
            <p>You will soon have to manage your own&nbsp;<strong>servers</strong> concept page hosted on remote&nbsp;<a href="https://intranet.alxswe.com/rltoken/nDPzEm5SYxcdGxP_OpVYXQ" title="data centers" target="_blank">data centers</a>. We need to set them up with your RSA public key so that you can access them via SSH.</p>
            <p>Create a RSA key pair.</p>
            <p>Requirements:</p>
            <ul>
                <li>Share your&nbsp;<strong>public key</strong> in your answer file&nbsp;<code>0-RSA_public_key.pub</code></li>
                <li>Fill the&nbsp;<code>SSH public key</code> field of your&nbsp;<a href="https://intranet.alxswe.com/rltoken/qsaEQ3ZWrgs-zoueDpXpPA" title="intranet profile" target="_blank">intranet profile</a> with the public key you just generated</li>
                <li><strong>Keep the private key to yourself in a secure location</strong>, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects</li>
                <li>If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase</li>
            </ul>
            <p>SSH and RSA keys will be covered in depth in a later project.</p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>0-RSA_public_key.pub</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>1. For Best School loop</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Bash script that displays&nbsp;<code>Best School</code> 10 times.</p>
            <p>Requirement:</p>
            <ul>
                <li>You must use the&nbsp;<code>for</code> loop (<code>while</code> and&nbsp;<code>until</code> are forbidden)</li>
            </ul>
            <pre><code>sylvain@ubuntu$ head -n 2 1-for_best_school 
#!/usr/bin/env bash
# This script is displaying &quot;Best School&quot; 10 times
sylvain@ubuntu$ ./1-for_best_school 
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
</code></pre>
            <p>Note that:</p>
            <ul>
                <li>The first line of my Bash script starts with&nbsp;<code>#!/usr/bin/env bash</code></li>
                <li>The second line of my Bash scripts is a comment explaining what it is doing</li>
            </ul>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>1-for_best_school</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>2. While Best School loop</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Bash script that displays&nbsp;<code>Best School</code> 10 times.</p>
            <p>Requirements:</p>
            <ul>
                <li>You must use the&nbsp;<code>while</code> loop (<code>for</code> and&nbsp;<code>until</code> are forbidden)</li>
            </ul>
            <pre><code>sylvain@ubuntu$ ./2-while_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>2-while_best_school</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>3. Until Best School loop</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Bash script that displays&nbsp;<code>Best School</code> 10 times.</p>
            <p>Requirements:</p>
            <ul>
                <li>You must use the&nbsp;<code>until</code> loop (<code>for</code> and&nbsp;<code>while</code> are forbidden)</li>
            </ul>
            <pre><code>sylvain@ubuntu$ ./3-until_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>3-until_best_school</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>4. If 9, say Hi!</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Bash script that displays&nbsp;<code>Best School</code> 10 times, but for the 9th iteration, displays&nbsp;<code>Best School</code> <em>and then</em> <code>Hi</code> on a new line.</p>
            <p>Requirements:</p>
            <ul>
                <li>You must use the&nbsp;<code>while</code> loop (<code>for</code> and&nbsp;<code>until</code> are forbidden)</li>
                <li>You must use the&nbsp;<code>if</code> statement</li>
            </ul>
            <pre><code>sylvain@ubuntu$ ./4-if_9_say_hi
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Hi
Best School
sylvain@ubuntu$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>4-if_9_say_hi</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>5. 4 bad luck, 8 is your chance</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Bash script that loops from 1 to 10 and:</p>
            <ul>
                <li>displays&nbsp;<code>bad luck</code> for the 4th loop iteration</li>
                <li>displays&nbsp;<code>good luck</code> for the 8th loop iteration</li>
                <li>displays&nbsp;<code>Best School</code> for the other iterations</li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>You must use the&nbsp;<code>while</code> loop (<code>for</code> and&nbsp;<code>until</code> are forbidden)</li>
                <li>You must use the&nbsp;<code>if</code>,&nbsp;<code>elif</code> and&nbsp;<code>else</code> statements</li>
            </ul>
            <pre><code>sylvain@ubuntu$ ./5-4_bad_luck_8_is_your_chance
Best School
Best School
Best School
bad luck
Best School
Best School
Best School
good luck
Best School
Best School
sylvain@ubuntu$ 
</code></pre>
            <p>For the most curious:</p>
            <ul>
                <li><a href="https://intranet.alxswe.com/rltoken/uhCfz6ariijQvbvmCyYRMg" title="8 in the Chinese culture" target="_blank">8 in the Chinese culture</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/WwpjD57ABmwWSfdUVcBhNg" title="4 in the Chinese culture" target="_blank">4 in the Chinese culture</a></li>
            </ul>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>5-4_bad_luck_8_is_your_chance</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>6. Superstitious numbers</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Bash script that displays numbers from 1 to 20 and:</p>
            <ul>
                <li>displays&nbsp;<code>4</code> <em>and then</em> <code>bad luck from China</code> for the 4th loop iteration</li>
                <li>displays&nbsp;<code>9</code> <em>and then</em> <code>bad luck from Japan</code> for the 9th loop iteration</li>
                <li>displays&nbsp;<code>17</code> <em>and then</em> <code>bad luck from Italy</code> for the 17th loop iteration</li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>You must use the&nbsp;<code>while</code> loop (<code>for</code> and&nbsp;<code>until</code> are forbidden)</li>
                <li>You must use the&nbsp;<code>case</code> statement</li>
            </ul>
            <pre><code>sylvain@ubuntu$ ./6-superstitious_numbers
1
2
3
4
bad luck from China
5
6
7
8
9
bad luck from Japan
10
11
12
13
14
15
16
17
bad luck from Italy
18
19
20
sylvain@ubuntu$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>6-superstitious_numbers</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>7. Clock</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Bash script that displays the time for 12 hours and 59 minutes:</p>
            <ul>
                <li>display hours from 0 to 12</li>
                <li>display minutes from 1 to 59</li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>You must use the&nbsp;<code>while</code> loop (<code>for</code> and&nbsp;<code>until</code> are forbidden)</li>
            </ul>
            <p>Note that in this example, we only display the first 70 lines using the&nbsp;<code>head</code> command.</p>
            <pre><code>sylvain@ubuntu$ ./7-clock | head -n 70
Hour: 0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
Hour: 1
1
2
3
4
5
6
7
8
9
sylvain@ubuntu$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>7-clock</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>8. For ls</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Bash script that displays:</p>
            <ul>
                <li>The content of the current directory</li>
                <li>In a list format</li>
                <li>Where only the part of the name after the first dash is displayed (refer to the example)</li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>You must use the&nbsp;<code>for</code> loop (<code>while</code> and&nbsp;<code>until</code> are forbidden)</li>
                <li>Do not display hidden files</li>
            </ul>
            <pre><code>sylvain@ubuntu$ ls
100-read_and_cut              1-for_best_school         6-superstitious_numbers
101-tell_the_story_of_passwd  2-while_best_school       7-clock
102-lets_parse_apache_logs    3-until_best_school       8-for_ls
103-dig_the-data              4-if_9_say_hi                  9-to_file_or_not_to_file
10-fizzbuzz                   5-4_bad_luck_8_is_your_chance
sylvain@ubuntu$  ./8-for_ls
read_and_cut
tell_the_story_of_passwd
lets_parse_apache_logs
dig_the-data
fizzbuzz
for_best_school
while_best_school
until_best_school
if_9_say_hi
4_bad_luck_8_is_your_chance
superstitious_numbers
clock
for_ls
to_file_or_not_to_file
sylvain@ubuntu$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>8-for_ls</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>9. To file, or not to file</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Bash script that gives you information about the&nbsp;<code>school</code> file.</p>
            <p>Requirements:</p>
            <ul>
                <li>You must use&nbsp;<code>if</code> and,&nbsp;<code>else</code> (<code>case</code> is forbidden)</li>
                <li>Your Bash script should check if the file exists and print:<ul>
                        <li>if the file exists:&nbsp;<code>school file exists</code></li>
                        <li>if the file does not exist:&nbsp;<code>school file does not exist</code></li>
                    </ul>
                </li>
                <li>If the file exists, print:<ul>
                        <li>if the file is empty:&nbsp;<code>school file is empty</code></li>
                        <li>if the file is not empty:&nbsp;<code>school file is not empty</code></li>
                        <li>if the file is a regular file:&nbsp;<code>school is a regular file</code></li>
                        <li>if the file is not a regular file: (nothing)</li>
                    </ul>
                </li>
            </ul>
            <pre><code>sylvain@ubuntu$ file school
school: cannot open `school&apos; (No such file or directory)
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
school file does not exist
sylvain@ubuntu$ touch school
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
school file exists
school file is empty
school is a regular file
sylvain@ubuntu$ echo &apos;betty&apos; &gt; school 
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
school file exists
school file is not empty
school is a regular file
sylvain@ubuntu$ rm school 
sylvain@ubuntu$ mkdir school
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
school file exists
school file is not empty
sylvain@ubuntu$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>9-to_file_or_not_to_file</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>10. FizzBuzz</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Bash script that displays numbers from 1 to 100.</p>
            <p>Requirements:</p>
            <ul>
                <li>Displays&nbsp;<code>FizzBuzz</code> when the number is a multiple of 3 and 5</li>
                <li>Displays&nbsp;<code>Fizz</code> when the number is multiple of 3</li>
                <li>Displays&nbsp;<code>Buzz</code> when the number is a multiple of 5</li>
                <li>Otherwise, displays the number</li>
                <li>In a list format</li>
            </ul>
            <pre><code>sylvain@ubuntu$ ./10-fizzbuzz | head -20
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
sylvain@ubuntu$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>10-fizzbuzz</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>11. Read and cut</h3>
            <div>#advanced</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>help:&nbsp;<code>read</code></p>
            <p>Write a Bash script that displays the content of the file&nbsp;<code>/etc/passwd</code>.</p>
            <p>Your script should only display:</p>
            <ul>
                <li>username</li>
                <li>user id</li>
                <li>Home directory path for the user</li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>You must use the&nbsp;<code>while</code> loop (<code>for</code> and&nbsp;<code>until</code> are forbidden)</li>
            </ul>
            <pre><code>sylvain@ubuntu$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
libuuid:x:100:101::/var/lib/libuuid:
syslog:x:101:104::/home/syslog:/bin/false
messagebus:x:102:106::/var/run/dbus:/bin/false
landscape:x:103:109::/var/lib/landscape:/bin/false
sshd:x:104:65534::/var/run/sshd:/usr/sbin/nologin
pollinate:x:105:1::/var/cache/pollinate:/bin/false
vagrant:x:1000:1000::/home/vagrant:/bin/bash
colord:x:106:112:colord colour management daemon,,,:/var/lib/colord:/bin/false
statd:x:107:65534::/var/lib/nfs:/bin/false
sylvain:98:99:Sylvain:/home/sylvain:/bin/bash
puppet:x:108:114:Puppet configuration management daemon,,,:/var/lib/puppet:/bin/false
ubuntu:x:1001:1001:Ubuntu:/home/ubuntu:/bin/bash
sylvain@ubuntu$ ./100-read_and_cut
root:0:/root
daemon:1:/usr/sbin
bin:2:/bin
sys:3:/dev
sync:4:/bin
games:5:/usr/games
man:6:/var/cache/man
lp:7:/var/spool/lpd
mail:8:/var/mail
news:9:/var/spool/news
uucp:10:/var/spool/uucp
proxy:13:/bin
www-data:33:/var/www
backup:34:/var/backups
list:38:/var/list
irc:39:/var/run/ircd
gnats:41:/var/lib/gnats
nobody:65534:/nonexistent
libuuid:100:/var/lib/libuuid
syslog:101:/home/syslog
messagebus:102:/var/run/dbus
landscape:103:/var/lib/landscape
sshd:104:/var/run/sshd
pollinate:105:/var/cache/pollinate
vagrant:1000:/home/vagrant
colord:106:/var/lib/colord
statd:107:/var/lib/nfs
sylvain:99:/bin/bash
puppet:108:/var/lib/puppet
ubuntu:1001:/home/ubuntu
sylvain@ubuntu$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>100-read_and_cut</code></li>
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
            <h3>12. Tell the story of passwd</h3>
            <div>#advanced</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/03ca27392c6338e696fc0c3b08765f02c98457a1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230501%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230501T150637Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=19ac1375f54cc95a8cf6304b3cc8abc36cd82f259819fb935849e6bcec68864d" alt=""></p>
            <p>Read:</p>
            <ul>
                <li><a href="https://intranet.alxswe.com/rltoken/8VeAz2XHCtuECDJ0PfMNIg" title="IFS (internal field separator)" target="_blank">IFS (internal field separator)</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/jm2-sSa3VlvI4zgRdreAsg" title="Understanding /etc/passwd" target="_blank">Understanding /etc/passwd</a></li>
            </ul>
            <p>The file&nbsp;<code>/etc/passwd</code> has already been covered in a&nbsp;<a href="https://intranet.alxswe.com/rltoken/5Y_b9prAxb_Y-l8xCaZwgQ" title="previous project" target="_blank">previous project</a> and you should be familiar with it. Today we will make up a story based on it.</p>
            <p>Write a Bash script that displays the content of the file&nbsp;<code>/etc/passwd</code>, using the&nbsp;<code>while</code> loop + IFS.</p>
            <p>Format:&nbsp;<code>The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID&apos;s place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO</code></p>
            <p>Requirements:</p>
            <ul>
                <li>You must use the&nbsp;<code>while</code> loop (<code>for</code> and&nbsp;<code>until</code> are forbidden)</li>
            </ul>
            <pre><code>sylvain@ubuntu$ ./101-tell_the_story_of_passwd
The user root is part of the 0 gang, lives in /root and rides /bin/bash. 0&apos;s place is protected by the passcode x, more info about the user here: root
The user daemon is part of the 1 gang, lives in /usr/sbin and rides /usr/sbin/nologin. 1&apos;s place is protected by the passcode x, more info about the user here: daemon
The user bin is part of the 2 gang, lives in /bin and rides /usr/sbin/nologin. 2&apos;s place is protected by the passcode x, more info about the user here: bin
The user sys is part of the 3 gang, lives in /dev and rides /usr/sbin/nologin. 3&apos;s place is protected by the passcode x, more info about the user here: sys
The user sync is part of the 65534 gang, lives in /bin and rides /bin/sync. 4&apos;s place is protected by the passcode x, more info about the user here: sync
The user games is part of the 60 gang, lives in /usr/games and rides /usr/sbin/nologin. 5&apos;s place is protected by the passcode x, more info about the user here: games
The user man is part of the 12 gang, lives in /var/cache/man and rides /usr/sbin/nologin. 6&apos;s place is protected by the passcode x, more info about the user here: man
The user lp is part of the 7 gang, lives in /var/spool/lpd and rides /usr/sbin/nologin. 7&apos;s place is protected by the passcode x, more info about the user here: lp
The user mail is part of the 8 gang, lives in /var/mail and rides /usr/sbin/nologin. 8&apos;s place is protected by the passcode x, more info about the user here: mail
The user news is part of the 9 gang, lives in /var/spool/news and rides /usr/sbin/nologin. 9&apos;s place is protected by the passcode x, more info about the user here: news
The user uucp is part of the 10 gang, lives in /var/spool/uucp and rides /usr/sbin/nologin. 10&apos;s place is protected by the passcode x, more info about the user here: uucp
The user proxy is part of the 13 gang, lives in /bin and rides /usr/sbin/nologin. 13&apos;s place is protected by the passcode x, more info about the user here: proxy
The user www-data is part of the 33 gang, lives in /var/www and rides /usr/sbin/nologin. 33&apos;s place is protected by the passcode x, more info about the user here: www-data
The user backup is part of the 34 gang, lives in /var/backups and rides /usr/sbin/nologin. 34&apos;s place is protected by the passcode x, more info about the user here: backup
The user list is part of the 38 gang, lives in /var/list and rides /usr/sbin/nologin. 38&apos;s place is protected by the passcode x, more info about the user here: Mailing List Manager
The user irc is part of the 39 gang, lives in /var/run/ircd and rides /usr/sbin/nologin. 39&apos;s place is protected by the passcode x, more info about the user here: ircd
The user gnats is part of the 41 gang, lives in /var/lib/gnats and rides /usr/sbin/nologin. 41&apos;s place is protected by the passcode x, more info about the user here: Gnats Bug-Reporting System (admin)
The user nobody is part of the 65534 gang, lives in /nonexistent and rides /usr/sbin/nologin. 65534&apos;s place is protected by the passcode x, more info about the user here: nobody
The user libuuid is part of the 101 gang, lives in /var/lib/libuuid and rides . 100&apos;s place is protected by the passcode x, more info about the user here: 
The user syslog is part of the 104 gang, lives in /home/syslog and rides /bin/false. 101&apos;s place is protected by the passcode x, more info about the user here: 
The user messagebus is part of the 106 gang, lives in /var/run/dbus and rides /bin/false. 102&apos;s place is protected by the passcode x, more info about the user here: 
The user landscape is part of the 109 gang, lives in /var/lib/landscape and rides /bin/false. 103&apos;s place is protected by the passcode x, more info about the user here: 
The user sshd is part of the 65534 gang, lives in /var/run/sshd and rides /usr/sbin/nologin. 104&apos;s place is protected by the passcode x, more info about the user here: 
The user pollinate is part of the 1 gang, lives in /var/cache/pollinate and rides /bin/false. 105&apos;s place is protected by the passcode x, more info about the user here: 
The user vagrant is part of the 1000 gang, lives in /home/vagrant and rides /bin/bash. 1000&apos;s place is protected by the passcode x, more info about the user here: 
The user colord is part of the 112 gang, lives in /var/lib/colord and rides /bin/false. 106&apos;s place is protected by the passcode x, more info about the user here: colord colour management daemon,,,
The user statd is part of the 65534 gang, lives in /var/lib/nfs and rides /bin/false. 107&apos;s place is protected by the passcode x, more info about the user here: 
The user puppet is part of the 114 gang, lives in /var/lib/puppet and rides /bin/false. 108&apos;s place is protected by the passcode x, more info about the user here: Puppet configuration management daemon,,,
The user ubuntu is part of the 1001 gang, lives in /home/ubuntu and rides /bin/bash. 1001&apos;s place is protected by the passcode x, more info about the user here: Ubuntu
sylvain@ubuntu$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>101-tell_the_story_of_passwd</code></li>
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
            <h3>13. Let&apos;s parse Apache logs</h3>
            <div>#advanced</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p><img src="https://intranet.alxswe.com/images/contents/sysadmin/projects/80/such_awk.jpg" alt=""></p>
            <p><a href="https://intranet.alxswe.com/rltoken/JfEwR2qcLdKkoihJNDZR0g" title="Apache" target="_blank">Apache</a> is among the most popular web servers in the world, serving 50% of all active websites, no doubt that you will have to interact with it within your career.</p>
            <p>As a Full-Stack Software Engineer, you have to master the art of parsing log files. Today we will do a simple parsing of&nbsp;<a href="http://intranet-projects-files.s3.amazonaws.com/holbertonschool-sysadmin_devops/80/apache-access.log" title="Apache log access files" target="_blank">Apache log access files</a>.</p>
            <p>Today the Customer Support department reported that a user reported that the site is being &ldquo;buggy&rdquo;. Not being a detailed description, you want to have a look at the Apache logs and gather data about the traffic.</p>
            <p>Write a Bash script that displays the visitor IP along with the&nbsp;<a href="https://intranet.alxswe.com/rltoken/7de-UBmf8xgwH1iSwzX1MA" title="HTTP status code" target="_blank">HTTP status code</a> from the Apache log file.</p>
            <p>Requirement:</p>
            <ul>
                <li>Format: IP HTTP_CODE<ul>
                        <li>in a list format</li>
                        <li>See example</li>
                    </ul>
                </li>
                <li>You must use&nbsp;<code>awk</code></li>
                <li>You are not allowed to use&nbsp;<code>while</code>,&nbsp;<code>for</code>,&nbsp;<code>until</code> and&nbsp;<code>cut</code></li>
                <li>Download and commit the&nbsp;<a href="https://intranet-projects-files.s3.amazonaws.com/holbertonschool-sysadmin_devops/80/apache-access.log" title="apache-access.log file" target="_blank">apache-access.log file</a> along with your answers files</li>
            </ul>
            <pre><code>sylvain@ubuntu$ ./102-lets_parse_apache_logs | tail -n 10
185.130.5.207 301
185.130.5.207 301
91.224.140.223 200
62.210.142.23 304
92.222.20.166 304
180.76.15.19 200
2.1.201.36 304
198.58.99.82 304
50.116.30.23 304
209.133.111.211 200
sylvain@ubuntu$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>102-lets_parse_apache_logs</code></li>
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
            <h3>14. Dig the data</h3>
            <div>#advanced</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Now that you&rsquo;ve parsed the Apache log file, let&rsquo;s sort the data so you can get a better idea of what is going on.</p>
            <p>Using what you did in the previous exercise, write a Bash script that groups visitors by IP and HTTP status code, and displays this data.</p>
            <p>Requirements:</p>
            <ul>
                <li>The exact format must be:<ul>
                        <li>OCCURENCE_NUMBER IP HTTP_CODE</li>
                        <li>In list format</li>
                    </ul>
                </li>
                <li>Ordered from the greatest to the lowest number of occurrences<ul>
                        <li>See example</li>
                    </ul>
                </li>
                <li>You must use&nbsp;<code>awk</code></li>
                <li>You are not allowed to use&nbsp;<code>while</code>,&nbsp;<code>for</code>,&nbsp;<code>until</code> and&nbsp;<code>cut</code></li>
            </ul>
            <pre><code>sylvain@ubuntu$ ./103-dig_the-data | head -n 10
    141 130.0.236.153 200
    140 62.210.250.66 200
    117 103.243.26.232 404
    67 195.154.172.143 200
    60 78.154.190.29 200
    45 195.154.172.59 200
    41 62.210.248.185 200
    41 167.114.156.198 200
    36 2.1.201.36 304
    36 195.154.172.53 200
sylvain@ubuntu$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x04-loops_conditions_and_parsing</code></li>
                    <li>File:&nbsp;<code>103-dig_the-data</code></li>
                </ul>
            </div>
        </div>
    </div>
</div>
