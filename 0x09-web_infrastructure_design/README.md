<h1>0x09. Web infrastructure design</h1>
<div>
    <div>DevOpsSysAdminweb infrastructure</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Sylvain Kalache, co-founder at Holberton School</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Project to be done in teams of&nbsp;3&nbsp;people&nbsp;(your team:&nbsp;Julius Njeri)</li>
        <li>&nbsp;Ongoing second chance project - started&nbsp;<span title="">May 25, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Jun 3, 2023 6:00 AM</span></li>
        <li>&nbsp;<strong>Manual QA review must be done</strong> (request it when you are done with the project)</li>
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
            <li><a href="https://intranet.alxswe.com/concepts/13">Monitoring</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/17">Web Server</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/33">Network basics</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/46">Load balancer</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/67">Server</a></li>
        </ul>
    </div>
</div>
<div>
    <div><iframe width="560" height="315" src="https://www.youtube.com/embed/lQNEW76KdYg" title="YouTube video player" frameborder="0" allowfullscreen=""></iframe>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><strong>Network basics</strong> concept page</li>
            <li><strong>Server</strong> concept page</li>
            <li><strong>Web server</strong> concept page</li>
            <li><strong>DNS</strong> concept page</li>
            <li><strong>Load balancer</strong> concept page</li>
            <li><strong>Monitoring</strong> concept page</li>
            <li><a href="https://intranet.alxswe.com/rltoken/n3CdS3EA5l5psDDKbEhApA" title="What is a database" target="_blank">What is a database</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/0as4wDlFqyhLhf0f_gedcw" title="What's the difference between a web server and an app server?" target="_blank">What&rsquo;s the difference between a web server and an app server?</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/Pl3UoEfAO7K_jUKRLMmnAQ" title="DNS record types" target="_blank">DNS record types</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/uxpx2YhXs10TFLIDg78chA" title="Single point of failure" target="_blank">Single point of failure</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/4ansLu2gtHnoFrNThqyObA" title="How to avoid downtime when deploying new code" target="_blank">How to avoid downtime when deploying new code</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/TAJeVYy9U9iLaEDd6XkbRA" title="High availability cluster (active-active/active-passive)" target="_blank">High availability cluster (active-active/active-passive)</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/c0zs2MxrmxFLsCPOizxq6g" title="What is HTTPS" target="_blank">What is HTTPS</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/j6idMcUTyNEDj1oYDQFmUw" title="What is a firewall" target="_blank">What is a firewall</a></li>
        </ul>
        <h2>Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/FPJvEE-DRJDvmVTNWeFR8A" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
        <h3>General</h3>
        <ul>
            <li>You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects</li>
            <li>You must be able to explain what each component is doing</li>
            <li>You must be able to explain system redundancy</li>
            <li>Know all the mentioned acronyms: LAMP, SPOF, QPS</li>
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
            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>For each task, once you are done whiteboarding (on a whiteboard, piece of paper or software or your choice), take a picture/screenshot of your diagram</li>
            <li>This project will be manually reviewed:</li>
            <li>As each task is completed, the name of that task will turn green</li>
            <li>Upload a screenshot, showing that you completed the required levels, to any image hosting service (I personally use&nbsp;<a href="https://intranet.alxswe.com/rltoken/m_O2HLsKrO1zg31LMcLOGQ" title="imgur" target="_blank">imgur</a> but feel free to use anything you want).</li>
            <li>For the following tasks, insert the link from of your screenshot into the answer file</li>
            <li>After pushing your answer file to GitHub, insert the GitHub file link into the URL box</li>
            <li>You will also have to whiteboard each task in front of a mentor, staff or student - no computer or notes will be allowed during the whiteboarding session</li>
            <li>Focus on what you are being asked:</li>
            <li>Cover what the requirements mention, we will explore details in a later project</li>
            <li>Keep in mind that you will have 30 minutes to perform the exercise, you will get points for what is asked in requirements</li>
            <li>Similarly in a job interview, you should answer what the interviewer asked for, be careful about being too verbose - always ask the interviewer if going into details is necessary - speaking too much can play against you</li>
            <li>In this project, again, avoid going in details if not asked</li>
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
<h2>Tasks</h2>
<div>
    <div>
        <div>
            <h3>0. Simple web stack</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a&nbsp;<a href="https://intranet.alxswe.com/rltoken/YVDX0XsC6XHp0nmezvT9vQ" title="LAMP stack" target="_blank">LAMP stack</a>.</p>
            <p>On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via&nbsp;<code>www.foobar.com</code>. Start your explanation by having a user wanting to access your website.</p>
            <p>Requirements:</p>
            <ul>
                <li>You must use:<ul>
                        <li>1 server</li>
                        <li>1 web server (Nginx)</li>
                        <li>1 application server</li>
                        <li>1 application files (your code base)</li>
                        <li>1 database (MySQL)</li>
                        <li>1 domain name&nbsp;<code>foobar.com</code> configured with a&nbsp;<code>www</code> record that points to your server IP&nbsp;<code>8.8.8.8</code></li>
                    </ul>
                </li>
                <li>You must be able to explain some specifics about this infrastructure:<ul>
                        <li>What is a server</li>
                        <li>What is the role of the domain name</li>
                        <li>What type of DNS record&nbsp;<code>www</code> is in&nbsp;<code>www.foobar.com</code></li>
                        <li>What is the role of the web server</li>
                        <li>What is the role of the application server</li>
                        <li>What is the role of the database</li>
                        <li>What is the server using to communicate with the computer of the user requesting the website</li>
                    </ul>
                </li>
                <li>You must be able to explain what the issues are with this infrastructure:<ul>
                        <li>SPOF</li>
                        <li>Downtime when maintenance needed (like deploying new code web server needs to be restarted)</li>
                        <li>Cannot scale if too much incoming traffic</li>
                    </ul>
                </li>
            </ul>
            <p>Please, remember that everything must be written in English to further your technical ability in a variety of settings.</p>
        </div>
        <div>
            <div>
                <div>
                    <h4>Add URLs here:</h4>
                    <div><input type="text" value=""><button type="button">Save</button></div>
                    <div><br></div>
                </div>
            </div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x09-web_infrastructure_design</code></li>
                    <li>File:&nbsp;<code>0-simple_web_stack</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>1. Distributed web infrastructure</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>On a whiteboard, design a three server web infrastructure that hosts the website&nbsp;<code>www.foobar.com</code>.</p>
            <p>Requirements:</p>
            <ul>
                <li>You must add:<ul>
                        <li>2 servers</li>
                        <li>1 web server (Nginx)</li>
                        <li>1 application server</li>
                        <li>1 load-balancer (HAproxy)</li>
                        <li>1 set of application files (your code base)</li>
                        <li>1 database (MySQL)</li>
                    </ul>
                </li>
                <li>You must be able to explain some specifics about this infrastructure:<ul>
                        <li>For every additional element, why you are adding it</li>
                        <li>What distribution algorithm your load balancer is configured with and how it works</li>
                        <li>Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both</li>
                        <li>How a database Primary-Replica (Master-Slave) cluster works</li>
                        <li>What is the difference between the Primary node and the Replica node in regard to the application</li>
                    </ul>
                </li>
                <li>You must be able to explain what the issues are with this infrastructure:<ul>
                        <li>Where are SPOF</li>
                        <li>Security issues (no firewall, no HTTPS)</li>
                        <li>No monitoring</li>
                    </ul>
                </li>
            </ul>
            <p>Please, remember that everything must be written in English to further your technical ability in a variety of settings.</p>
        </div>
        <div>
            <div>
                <div>
                    <h4>Add URLs here:</h4>
                    <div><input type="text" value=""><button type="button">Save</button></div>
                    <div><br></div>
                </div>
            </div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x09-web_infrastructure_design</code></li>
                    <li>File:&nbsp;<code>1-distributed_web_infrastructure</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>2. Secured and monitored web infrastructure</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>On a whiteboard, design a three server web infrastructure that hosts the website&nbsp;<code>www.foobar.com</code>, it must be secured, serve encrypted traffic, and be monitored.</p>
            <p>Requirements:</p>
            <ul>
                <li>You must add:<ul>
                        <li>3 firewalls</li>
                        <li>1 SSL certificate to serve&nbsp;<code>www.foobar.com</code> over HTTPS</li>
                        <li>3 monitoring clients (data collector for Sumologic or other monitoring services)</li>
                    </ul>
                </li>
                <li>You must be able to explain some specifics about this infrastructure:<ul>
                        <li>For every additional element, why you are adding it</li>
                        <li>What are firewalls for</li>
                        <li>Why is the traffic served over HTTPS</li>
                        <li>What monitoring is used for</li>
                        <li>How the monitoring tool is collecting data</li>
                        <li>Explain what to do if you want to monitor your web server QPS</li>
                    </ul>
                </li>
                <li>You must be able to explain what the issues are with this infrastructure:<ul>
                        <li>Why terminating SSL at the load balancer level is an issue</li>
                        <li>Why having only one MySQL server capable of accepting writes is an issue</li>
                        <li>Why having servers with all the same components (database, web server and application server) might be a problem</li>
                    </ul>
                </li>
            </ul>
            <p>Please, remember that everything must be written in English to further your technical ability in a variety of settings.</p>
        </div>
        <div>
            <div>
                <div>
                    <h4>Add URLs here:</h4>
                    <div><input type="text" value=""><button type="button">Save</button></div>
                    <div><br></div>
                </div>
            </div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x09-web_infrastructure_design</code></li>
                    <li>File:&nbsp;<code>2-secured_and_monitored_web_infrastructure</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>3. Scale up</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Readme</p>
            <ul>
                <li><a href="https://intranet.alxswe.com/rltoken/toFi_SdFHyi2MaELB8ekqw" title="Application server vs web server" target="_blank">Application server vs web server</a></li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>You must add:<ul>
                        <li>1 server</li>
                        <li>1 load-balancer (HAproxy) configured as cluster with the other one</li>
                        <li>Split components (web server, application server, database) with their own server</li>
                    </ul>
                </li>
                <li>You must be able to explain some specifics about this infrastructure:<ul>
                        <li>For every additional element, why you are adding it</li>
                    </ul>
                </li>
            </ul>
            <p>Please, remember that everything must be written in English to further your technical ability in a variety of settings.</p>
        </div>
        <div>
            <div>
                <div>
                    <h4>Add URLs here:</h4>
                    <div><input type="text" value=""><button type="button">Save</button></div>
                    <div><br></div>
                </div>
            </div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x09-web_infrastructure_design</code></li>
                    <li>File:&nbsp;<code>3-scale_up</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button>&nbsp;</div>
            </div>
        </div>
    </div>
</div>
