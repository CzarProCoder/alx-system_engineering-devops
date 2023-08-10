<h1>0x18. Webstack monitoring</h1>
<div>
    <div>DevOpsSysAdminmonitoring</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Sylvain Kalache, co-founder at Holberton School</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Ongoing second chance project - started&nbsp;<span title="">Aug 9, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Aug 11, 2023 6:00 AM</span></li>
        <li>&nbsp;An auto review will be launched at the deadline</li>
    </ul>
</div>
<div>
    <h4>In a nutshell&hellip;</h4>
    <ul>
        <li><strong>Auto QA review:</strong> 0.0/12 mandatory</li>
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
        <h3>Concepts</h3>
    </div>
    <div>
        <p><em>For this project, we expect you to look at these concepts:</em></p>
        <ul>
            <li><a href="https://intranet.alxswe.com/concepts/13">Monitoring</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/67">Server</a></li>
        </ul>
    </div>
</div>
<div>
    <div>
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/hb3pAsO.png" alt=""></p>
        <h2>Background Context</h2>
        <p>&ldquo;You cannot fix or improve what you cannot measure&rdquo; is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.</p>
        <p>Web stack monitoring can be broken down into 2 categories:</p>
        <ul>
            <li>Application monitoring: getting data about your running software and making sure it is behaving as expected</li>
            <li>Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)</li>
        </ul>
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/ktCXnhE.jpg" alt=""></p>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/km_XUDAfXEBoXZQsIWEo5Q" title="What is server monitoring" target="_blank">What is server monitoring</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/z9jsikINjrsUo2QY5_Xz8g" title="What is application monitoring" target="_blank">What is application monitoring</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/_8KIbIUNzMgKi_LiGMBWAw" title="System monitoring by Google" target="_blank">System monitoring by Google</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/V3GsrDcMHPdgrizShj4RCg" title="Nginx logging and monitoring" target="_blank">Nginx logging and monitoring</a></li>
        </ul>
        <h2>Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/Bd9r8twsVT3S_8j7-kOLrg" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
        <h3>General</h3>
        <ul>
            <li>Why is monitoring needed</li>
            <li>What are the 2 main area of monitoring</li>
            <li>What are access logs for a web server (such as Nginx)</li>
            <li>What are error logs for a web server (such as Nginx)</li>
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
                    <td><code>54.161.241.209</code></td>
                    <td>running</td>
                    <td>
                        <div><button type="button">Actions&nbsp;Toggle Dropdown</button></div>
                    </td>
                </tr>
                <tr>
                    <td>196617-web-02</td>
                    <td><code>ubuntu</code></td>
                    <td><code>54.174.176.238</code></td>
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
            <h3>0. Sign up for Datadog and install datadog-agent</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>For this task head to&nbsp;<a href="https://intranet.alxswe.com/rltoken/Ufs6rTHMET5LB1Uoylx0nw" title="https://www.datadoghq.com/" target="_blank">https://www.datadoghq.com/</a> and sign up for a free&nbsp;<code>Datadog</code> account. When signing up, you&rsquo;ll have the option of selecting statistics from your current stack that&nbsp;<code>Datadog</code> can monitor for you. Once you have an account set up, follow the instructions given on the website to install the&nbsp;<code>Datadog</code> agent.</p>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6b0ea6345a6375437845.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230810%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230810T193701Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=eac220ca430604e3dda15ab8ebfd6b090af7a32810d4af5825c1d75b51ca7d23" alt=""></p>
            <ul>
                <li>Sign up for Datadog -&nbsp;<strong>Please make sure you are using the US website of Datagog (https://app.datadoghq.com)</strong></li>
                <li>Use the&nbsp;<strong>US1</strong> region</li>
                <li>Install&nbsp;<code>datadog-agent</code> on&nbsp;<code>web-01</code></li>
                <li>Create an&nbsp;<code>application key</code></li>
                <li>Copy-paste in your Intranet user profile (<a href="https://intranet.alxswe.com/rltoken/elXu5CcaGpeK7GxerBb7wQ" title="here" target="_blank">here</a>) your DataDog&nbsp;<code>API key</code> and your DataDog&nbsp;<code>application key</code>.</li>
                <li>Your server&nbsp;<code>web-01</code> should be visible in Datadog under the host name&nbsp;<code>XX-web-01</code>
                    <ul>
                        <li>You can validate it by using this&nbsp;<a href="https://intranet.alxswe.com/rltoken/5BtVPmgzhb96y7jZDGGHOQ" title="API" target="_blank">API</a></li>
                        <li>If needed, you will need to update the hostname of your server</li>
                    </ul>
                </li>
            </ul>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x18-webstack_monitoring</code></li>
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
            <h3>1. Monitor some metrics</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some&nbsp;<code>monitors</code> within the&nbsp;<code>Datadog</code> dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here:&nbsp;<a href="https://intranet.alxswe.com/rltoken/4RPOEVDTqKXuvyU4Gkj2Bw" title="System Check" target="_blank">System Check</a>.</p>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6a4551974aadc181e97a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230810%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230810T193701Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=640c1646ecf710361d38ecf06b106eab9f1bb6d294fec02372f3817e012e688c" alt=""></p>
            <ul>
                <li>Set up a monitor that checks the number of read requests issued to the device per second.</li>
                <li>Set up a monitor that checks the number of write requests issued to the device per second.</li>
            </ul>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x18-webstack_monitoring</code></li>
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
            <h3>2. Create a dashboard</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Now create a dashboard with different metrics displayed in order to get a few different visualizations.</p>
            <ul>
                <li>Create a new&nbsp;<code>dashboard</code></li>
                <li>Add at least 4&nbsp;<code>widgets</code> to your dashboard. They can be of any type and monitor whatever you&rsquo;d like</li>
                <li>Create the answer file&nbsp;<code>2-setup_datadog</code> which has the&nbsp;<code>dashboard_id</code> on the first line.&nbsp;<strong>Note</strong>: in order to get the id of your dashboard, you may need to use&nbsp;<a href="https://intranet.alxswe.com/rltoken/QhlPcQqUocwWcOkZ9s4mWQ" title="Datadog's API" target="_blank">Datadog&rsquo;s API</a></li>
            </ul>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x18-webstack_monitoring</code></li>
                    <li>File:&nbsp;<code>2-setup_datadog</code></li>
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
