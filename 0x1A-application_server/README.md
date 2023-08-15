<h1>0x1A. Application server</h1>
<div>
    <div>DevOpsSysAdmin</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Sylvain Kalache, co-founder at Holberton School</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Project will start&nbsp;<span title="">Aug 14, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Aug 18, 2023 6:00 AM</span></li>
        <li>&nbsp;Checker&nbsp;will be&nbsp;released at&nbsp;<span title="">Aug 16, 2023 8:24 PM</span></li>
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
            <li><a href="https://intranet.alxswe.com/concepts/67">Server</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/68">Web stack debugging</a></li>
        </ul>
    </div>
</div>
<div>
    <div>
        <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230815T083128Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=69dd7d909e48ec1c75c5f52008c099cfbe8edc6e6d1c3462186b465ddf93db5e" alt=""></p>
        <h2>Background Context</h2>
        <p><a href="https://youtu.be/pSrKT7m4Ego" target="_blank"><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/2ea1058f813d42c61f48.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230815T083128Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=573f10c64523659b25cc2cd532c08016a5cbaaddfe3b94c39ada033ba59b6aa0" alt=""></a></p>
        <p>Your web infrastructure is already serving web pages via&nbsp;<code>Nginx</code> that you installed in your&nbsp;<a href="https://intranet.alxswe.com/rltoken/95oRNZ-zRGwLxtWECJqsWA" title="first web stack project" target="_blank">first web stack project</a>. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your&nbsp;<code>Nginx</code> and make is serve your Airbnb clone project.</p>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/B9fOBzIxX_t1289WAuRzJw" title="Application server vs web server" target="_blank">Application server vs web server</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/kpG6RwmwRJHzRmGUM_ERcA" title="How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04" target="_blank">How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04</a> (As mentioned in the video, do&nbsp;<strong>not</strong> install Gunicorn using&nbsp;<code>virtualenv</code>, just install everything globally)</li>
            <li><a href="https://intranet.alxswe.com/rltoken/2LF1j7xKJGYaUtD1HKgUeQ" title="Running Gunicorn" target="_blank">Running Gunicorn</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/lEg0zpkkDcLtdl3VD4ACRQ" title="Be careful with the way Flask manages slash" target="_blank">Be careful with the way Flask manages slash</a> in&nbsp;<a href="https://intranet.alxswe.com/rltoken/Zn8fYk-U9YRm7Z5Coqqb0g" title="route" target="_blank">route</a> -&nbsp;<code>strict_slashes</code></li>
            <li><a href="https://intranet.alxswe.com/rltoken/cldrneY3Qr7LlDysygzRHw" title="Upstart documentation" target="_blank">Upstart documentation</a></li>
        </ul>
        <h2>Requirements</h2>
        <h3>General</h3>
        <ul>
            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>Everything Python-related must be done using&nbsp;<code>python3</code></li>
            <li>All config files must have comments</li>
        </ul>
        <h3>Bash Scripts</h3>
        <ul>
            <li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
            <li>All your files should end with a new line</li>
            <li>All your Bash script files must be executable</li>
            <li>Your Bash script must pass&nbsp;<code>Shellcheck</code> (version&nbsp;<code>0.3.7-5~ubuntu16.04.1</code> via&nbsp;<code>apt-get</code>) without any error</li>
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
            <h3>0. Set up development with Python</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Let&rsquo;s serve what you built for&nbsp;<a href="https://intranet.alxswe.com/rltoken/uEAW4JG-DyhtSjYNP9o1mQ" title="AirBnB clone v2 - Web framework" target="_blank">AirBnB clone v2 - Web framework</a> on&nbsp;<code>web-01</code>. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.</p>
            <p>Requirements:</p>
            <ul>
                <li>Make sure that&nbsp;<a href="https://intranet.alxswe.com/rltoken/ecvps9dI2mv1QUu3dn99mA" title="task #3" target="_blank">task #3</a> of your&nbsp;<a href="https://intranet.alxswe.com/rltoken/7-lshY-qe4ZxKabnC7pY4Q" title="SSH project" target="_blank">SSH project</a> is completed for&nbsp;<code>web-01</code>. The checker will connect to your servers.</li>
                <li>Install the&nbsp;<code>net-tools</code> package on your server:&nbsp;<code>sudo apt install -y net-tools</code></li>
                <li>Git clone your&nbsp;<code>AirBnB_clone_v2</code> on your&nbsp;<code>web-01</code> server.</li>
                <li>Configure the file&nbsp;<code>web_flask/0-hello_route.py</code> to serve its content from the route&nbsp;<code>/airbnb-onepage/</code> on port&nbsp;<code>5000</code>.</li>
                <li>Your Flask application object must be named&nbsp;<code>app</code> (This will allow us to run and check your code).</li>
            </ul>
            <p>Example:</p>
            <h5>Window 1:</h5>
            <pre><code>ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app &quot;0-hello_route&quot; (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
35.231.193.217 - - [02/May/2019 22:19:42] &quot;GET /airbnb-onepage/ HTTP/1.1&quot; 200 -
</code></pre>
            <h5>Window 2:</h5>
            <pre><code>ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x1A-application_server</code></li>
                    <li>File:&nbsp;<code>README.md</code></li>
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
            <h3>1. Set up production with Gunicorn</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Now that you have your development environment set up, let&rsquo;s get your production application server set up with&nbsp;<code>Gunicorn</code> on&nbsp;<code>web-01</code>, port&nbsp;<code>5000</code>. You&rsquo;ll need to install&nbsp;<code>Gunicorn</code> and any libraries required by your application. Your&nbsp;<code>Flask</code> application object will serve as a&nbsp;<a href="https://intranet.alxswe.com/rltoken/IaAZ7A8IYGkO9Ah9uwL39Q" title="WSGI" target="_blank">WSGI</a> entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.</p>
            <p>Requirements:</p>
            <ul>
                <li>Install&nbsp;<code>Gunicorn</code> and any other libraries required by your application.</li>
                <li>The Flask application object should be called&nbsp;<code>app</code>. (This will allow us to run and check your code)</li>
                <li>You will serve the same content from the same route as in the previous task. You can verify that it&rsquo;s working by binding a&nbsp;<code>Gunicorn</code> instance to localhost listening on port&nbsp;<code>5000</code> with your application object as the entry point.</li>
                <li>In order to check your code, the checker will bind a&nbsp;<code>Gunicorn</code> instance to port&nbsp;<code>6000</code>, so make sure nothing is listening on that port.</li>
            </ul>
            <p>Example:</p>
            <h5>Terminal 1:</h5>
            <pre><code>ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-03 20:47:20 +0000] [3595] [INFO] Starting gunicorn 19.9.0
[2019-05-03 20:47:20 +0000] [3595] [INFO] Listening at: http://0.0.0.0:5000 (3595)
[2019-05-03 20:47:20 +0000] [3595] [INFO] Using worker: sync
[2019-05-03 20:47:20 +0000] [3598] [INFO] Booting worker with pid: 3598
</code></pre>
            <h5>Terminal 2:</h5>
            <pre><code>ubuntu@229-web-01:~$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x1A-application_server</code></li>
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
            <h3>2. Serve a page with Nginx</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Building on your work in the previous tasks, configure&nbsp;<code>Nginx</code> to serve your page from the route&nbsp;<code>/airbnb-onepage/</code></p>
            <p>Requirements:</p>
            <ul>
                <li><code>Nginx</code> must serve this page both locally and on its public IP on port&nbsp;<code>80</code>.</li>
                <li><code>Nginx</code> should proxy requests to the process listening on port&nbsp;<code>5000</code>.</li>
                <li>Include your&nbsp;<code>Nginx</code> config file as&nbsp;<code>2-app_server-nginx_config</code>.</li>
            </ul>
            <p>Notes:</p>
            <ul>
                <li>In order to test this you&rsquo;ll have to spin up either your production or development application server (listening on port&nbsp;<code>5000</code>)</li>
                <li>In an actual production environment the application server will be configured to start upon startup in a system initialization script. This will be covered in the advanced tasks.</li>
                <li>You will probably need to&nbsp;<code>reboot</code> your server (by using the command&nbsp;<code>$ sudo reboot</code>) to have Nginx publicly accessible</li>
            </ul>
            <p>Example:</p>
            <h4>On my server:</h4>
            <h5>Window 1:</h5>
            <pre><code>ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-06 20:43:57 +0000] [14026] [INFO] Starting gunicorn 19.9.0
[2019-05-06 20:43:57 +0000] [14026] [INFO] Listening at: http://0.0.0.0:5000 (14026)
[2019-05-06 20:43:57 +0000] [14026] [INFO] Using worker: sync
[2019-05-06 20:43:57 +0000] [14029] [INFO] Booting worker with pid: 14029
</code></pre>
            <h5>Window 2:</h5>
            <pre><code>ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
</code></pre>
            <h4>On my local terminal:</h4>
            <pre><code>vagrant@ubuntu-xenial:~$ curl -sI 35.231.193.217/airbnb-onepage/
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Mon, 06 May 2019 20:44:55 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 11
Connection: keep-alive
X-Served-By: 229-web-01

vagrant@ubuntu-xenial:~$ curl 35.231.193.217/airbnb-onepage/
Hello HBNB!vagrant@ubuntu-xenial:~$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x1A-application_server</code></li>
                    <li>File:&nbsp;<code>2-app_server-nginx_config</code></li>
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
            <h3>3. Add a route with query parameters</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Building on what you did in the previous tasks, let&rsquo;s expand our web application by adding another service for&nbsp;<code>Gunicorn</code> to handle. In&nbsp;<code>AirBnB_clone_v2/web_flask/6-number_odd_or_even</code>, the route&nbsp;<code>/number_odd_or_even/&lt;int:n&gt;</code> should already be defined to render a page telling you whether an integer is odd or even. You&rsquo;ll need to configure&nbsp;<code>Nginx</code> to proxy HTTP requests to the route&nbsp;<code>/airbnb-dynamic/number_odd_or_even/(any integer)</code> to a&nbsp;<code>Gunicorn</code> instance listening on port&nbsp;<code>5001</code>. The key to this exercise is getting&nbsp;<code>Nginx</code> configured to proxy requests to processes listening on two different ports. You are not expected to keep your application server processes running. If you want to know how to run multiple instances of&nbsp;<code>Gunicorn</code> without having multiple terminals open, see tips below.</p>
            <p>Requirements:</p>
            <ul>
                <li><code>Nginx</code> must serve this page both locally and on its public IP on port&nbsp;<code>80</code>.</li>
                <li><code>Nginx</code> should proxy requests to the route&nbsp;<code>/airbnb-dynamic/number_odd_or_even/(any integer)</code> the process listening on port&nbsp;<code>5001</code>.</li>
                <li>Include your&nbsp;<code>Nginx</code> config file as&nbsp;<code>3-app_server-nginx_config</code>.</li>
            </ul>
            <p>Tips:</p>
            <ul>
                <li>Check out these articles/docs for clues on how to configure&nbsp;<code>Nginx</code>:&nbsp;<a href="https://intranet.alxswe.com/rltoken/0xFZ6umndhIH19cSGFnexg" title="Understanding Nginx Server and Location Block Selection Algorithms" target="_blank">Understanding Nginx Server and Location Block Selection Algorithms</a>,&nbsp;<a href="https://intranet.alxswe.com/rltoken/ogjtMopkJjRSToliXzemGQ" title="Understanding Nginx Location Blocks Rewrite Rules" target="_blank">Understanding Nginx Location Blocks Rewrite Rules</a>,&nbsp;<a href="https://intranet.alxswe.com/rltoken/8O-01TMh2X22EmYNps0X-Q" title="Nginx Reverse Proxy" target="_blank">Nginx Reverse Proxy</a>.</li>
                <li>In order to spin up a&nbsp;<code>Gunicorn</code> instance as a detached process you can use the terminal multiplexer utility&nbsp;<code>tmux</code>. Enter the command&nbsp;<code>tmux new-session -d &apos;gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app&apos;</code> and if successful you should see no output to the screen. You can verify that the process has been created by running&nbsp;<code>pgrep gunicorn</code> to see its PID. Once you&rsquo;re ready to end the process you can either run&nbsp;<code>tmux a</code> to reattach to the processes, or you can run&nbsp;<code>kill &lt;PID&gt;</code> to terminate the background process by ID.</li>
            </ul>
            <p>Example:</p>
            <h5>Terminal 1:</h5>
            <pre><code>ubuntu@229-web-01:~/AirBnB_clone_v2$ tmux new-session -d &apos;gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app&apos;
ubuntu@229-web-01:~/AirBnB_clone_v2$ pgrep gunicorn
1661
1665
ubuntu@229-web-01:~/AirBnB_clone_v2$ tmux new-session -d &apos;gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app&apos;
ubuntu@229-web-01:~/AirBnB_clone_v2$ pgrep gunicorn
1661
1665
1684
1688

ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$

ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5001/number_odd_or_even/6
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
  &lt;HEAD&gt;
    &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
  &lt;/HEAD&gt;
  &lt;BODY&gt;&lt;H1&gt;Number: 6 is even&lt;/H1&gt;&lt;/BODY&gt;
&lt;/HTML&gt;ubuntu@229-web-01:~/AirBnB_clone_v2
ubuntu@229-web-01:~$ 
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1/airbnb-dynamic/number_odd_or_even/5
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
  &lt;HEAD&gt;
    &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
  &lt;/HEAD&gt;
  &lt;BODY&gt;&lt;H1&gt;Number: 5 is odd&lt;/H1&gt;&lt;/BODY&gt;
&lt;/HTML&gt;ubuntu@229-web-01:~/AirBnB_clone_v2$
</code></pre>
            <h5>Local machine:</h5>
            <pre><code>vagrant@ubuntu-xenial:~$ curl 35.231.193.217/airbnb-dynamic/number_odd_or_even/6&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
  &lt;HEAD&gt;
    &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
  &lt;/HEAD&gt;
  &lt;BODY&gt;&lt;H1&gt;Number: 6 is even&lt;/H1&gt;&lt;/BODY&gt;
&lt;/HTML&gt;vagrant@ubuntu-xenial:~$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x1A-application_server</code></li>
                    <li>File:&nbsp;<code>3-app_server-nginx_config</code></li>
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
            <h3>4. Let&apos;s do this for your API</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Let&rsquo;s serve what you built for&nbsp;<a href="https://intranet.alxswe.com/rltoken/QXJ9ryafcRfd_cARiugRiQ" title="AirBnB clone v3 - RESTful API" target="_blank">AirBnB clone v3 - RESTful API</a> on&nbsp;<code>web-01</code>.</p>
            <p>Requirements:</p>
            <ul>
                <li>Git clone your&nbsp;<code>AirBnB_clone_v3</code></li>
                <li>Setup&nbsp;<code>Nginx</code> so that the route&nbsp;<code>/api/</code> points to a&nbsp;<code>Gunicorn</code> instance listening on port&nbsp;<code>5002</code></li>
                <li><code>Nginx</code> must serve this page both locally and on its public IP on port&nbsp;<code>80</code></li>
                <li>To test your setup you should bind&nbsp;<code>Gunicorn</code> to&nbsp;<code>api/v1/app.py</code></li>
                <li>It may be helpful to import your data (and environment variables) from&nbsp;<a href="https://intranet.alxswe.com/rltoken/ZSQFQJPNTKrRdXynG6PWEw" title="this project" target="_blank">this project</a></li>
                <li>Upload your&nbsp;<code>Nginx</code> config file as&nbsp;<code>4-app_server-nginx_config</code></li>
            </ul>
            <p>Example:</p>
            <h5>Terminal 1:</h5>
            <pre><code>ubuntu@229-web-01:~/AirBnB_clone_v3$ tmux new-session -d &apos;gunicorn --bind 0.0.0.0:5002 api.v1.app:app&apos;
ubuntu@229-web-01:~/AirBnB_clone_v3$ curl 127.0.0.1:5002/api/v1/states
[{&quot;__class__&quot;:&quot;State&quot;,&quot;created_at&quot;:&quot;2019-05-10T00:39:27.032802&quot;,&quot;id&quot;:&quot;7512f664-4951-4231-8de9-b18d940cc912&quot;,&quot;name&quot;:&quot;California&quot;,&quot;updated_at&quot;:&quot;2019-05-10T00:39:27.032965&quot;},{&quot;__class__&quot;:&quot;State&quot;,&quot;created_at&quot;:&quot;2019-05-10T00:39:36.021219&quot;,&quot;id&quot;:&quot;b25625c8-8a7a-4c1f-8afc-257bf9f76bc8&quot;,&quot;name&quot;:&quot;Arizona&quot;,&quot;updated_at&quot;:&quot;2019-05-10T00:39:36.021281&quot;}]
ubuntu@229-web-01:~/AirBnB_clone_v3$
ubuntu@229-web-01:~/AirBnB_clone_v3$ curl 127.0.0.1/api/v1/states
[{&quot;__class__&quot;:&quot;State&quot;,&quot;created_at&quot;:&quot;2019-05-10T00:39:27.032802&quot;,&quot;id&quot;:&quot;7512f664-4951-4231-8de9-b18d940cc912&quot;,&quot;name&quot;:&quot;California&quot;,&quot;updated_at&quot;:&quot;2019-05-10T00:39:27.032965&quot;},{&quot;__class__&quot;:&quot;State&quot;,&quot;created_at&quot;:&quot;2019-05-10T00:39:36.021219&quot;,&quot;id&quot;:&quot;b25625c8-8a7a-4c1f-8afc-257bf9f76bc8&quot;,&quot;name&quot;:&quot;Arizona&quot;,&quot;updated_at&quot;:&quot;2019-05-10T00:39:36.021281&quot;}]
ubuntu@229-web-01:~/AirBnB_clone_v3$
</code></pre>
            <h5>Local Terminal:</h5>
            <pre><code>vagrant@ubuntu-xenial:~$ curl 35.231.193.217/api/v1/states
[{&quot;__class__&quot;:&quot;State&quot;,&quot;created_at&quot;:&quot;2019-05-10T00:39:27.032802&quot;,&quot;id&quot;:&quot;7512f664-4951-4231-8de9-b18d940cc912&quot;,&quot;name&quot;:&quot;California&quot;,&quot;updated_at&quot;:&quot;2019-05-10T00:39:27.032965&quot;},{&quot;__class__&quot;:&quot;State&quot;,&quot;created_at&quot;:&quot;2019-05-10T00:39:36.021219&quot;,&quot;id&quot;:&quot;b25625c8-8a7a-4c1f-8afc-257bf9f76bc8&quot;,&quot;name&quot;:&quot;Arizona&quot;,&quot;updated_at&quot;:&quot;2019-05-10T00:39:36.021281&quot;}]
vagrant@ubuntu-xenial:~$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x1A-application_server</code></li>
                    <li>File:&nbsp;<code>4-app_server-nginx_config</code></li>
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
            <h3>5. Serve your AirBnB clone</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Let&rsquo;s serve what you built for&nbsp;<a href="https://intranet.alxswe.com/rltoken/RxqcMPx7OaDUPPtQfGJDUg" title="AirBnB clone - Web dynamic" target="_blank">AirBnB clone - Web dynamic</a> on&nbsp;<code>web-01</code>.</p>
            <p>Requirements:</p>
            <ul>
                <li>Git clone your&nbsp;<code>AirBnB_clone_v4</code></li>
                <li>Your&nbsp;<code>Gunicorn</code> instance should serve content from&nbsp;<code>web_dynamic/2-hbnb.py</code> on port&nbsp;<code>5003</code></li>
                <li>Setup&nbsp;<code>Nginx</code> so that the route&nbsp;<code>/</code> points to your&nbsp;<code>Gunicorn</code> instance</li>
                <li>Setup&nbsp;<code>Nginx</code> so that it properly serves the static assets found in&nbsp;<code>web_dynamic/static/</code> (this is essential for your page to render properly)</li>
                <li>For your website to be fully functional, you will need to reconfigure&nbsp;<code>web_dynamic/static/scripts/2-hbnb.js</code> to the correct IP</li>
                <li><code>Nginx</code> must serve this page both locally and on its public IP and port&nbsp;<code>5003</code></li>
                <li>Make sure to pull up your Developer Tools on your favorite browser to verify that you have no errors</li>
                <li>Upload your&nbsp;<code>Nginx</code> config as&nbsp;<code>5-app_server-nginx_config</code></li>
            </ul>
            <p>After loading, your website should look like this:</p>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/7a8a7c33021b1b74f9cdc1fd8f855bdb1f8cd44e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230815T083128Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=443820fd79a468c560564423bf4c2aa1e1d74e72068231dcb06291c8601b3ed7" alt=""></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x1A-application_server</code></li>
                    <li>File:&nbsp;<code>5-app_server-nginx_config</code></li>
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
            <h3>6. Deploy it!</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Once you&rsquo;ve got your application server configured, you want to set it up to run by default when Linux is booted. This way when your server inevitably requires downtime (you have to shut it down or restart it for one reason or another), your&nbsp;<code>Gunicorn</code> process(es) will start up as part of the system initialization process, freeing you from having to manually restart them. For this we will use&nbsp;<code>systemd</code>. You can read more about&nbsp;<code>systemd</code> in the documentation posted at the top of this project but to put it succinctly, it is a system initialization daemon for the Linux OS (amongst other things). For this task you will write a&nbsp;<code>systemd</code> script which will start your application server for you. As mentioned in the video at the top of the project, you do not need to create a Unix socket to bind the process to.</p>
            <p><strong>Requirements:</strong></p>
            <ul>
                <li>Write a&nbsp;<code>systemd</code> script which starts a&nbsp;<code>Gunicorn</code> process to serve the same content as the previous task (<code>web_dynamic/2-hbnb.py</code>)</li>
                <li>The&nbsp;<code>Gunicorn</code> process should spawn 3 worker processes</li>
                <li>The process should log errors in&nbsp;<code>/tmp/airbnb-error.log</code></li>
                <li>The process should log access in&nbsp;<code>/tmp/airbnb-access.log</code></li>
                <li>The process should be bound to port&nbsp;<code>5003</code></li>
                <li>Your&nbsp;<code>systemd</code> script should be stored in the appropriate directory on&nbsp;<code>web-01</code></li>
                <li>Make sure that you start the&nbsp;<code>systemd</code> service and leave it running</li>
                <li>Upload&nbsp;<code>gunicorn.service</code> to GitHub</li>
            </ul>
            <pre><code>bob@dylan:~$ curl -s 127.0.0.1:5003/2-hbnb | tail -5
    &lt;/div&gt;
    &lt;footer&gt;
      &lt;p&gt;Holberton School&lt;/p&gt;
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
bob@dylan:~$ 
bob@dylan:~$ curl -s 12.13.14.15/ | tail -5
    &lt;/div&gt;
    &lt;footer&gt;
      &lt;p&gt;Holberton School&lt;/p&gt;
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
bob@dylan:~$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x1A-application_server</code></li>
                    <li>File:&nbsp;<code>gunicorn.service</code></li>
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
            <h3>7. No service interruption</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>One of the most important metrics for any Internet-based business is its uptime. It is the percentage of the time over a given period that the service/product is accessible to customers. Let&rsquo;s pick the example of Amazon.com, for every minute of downtime (which is the opposite of uptime),&nbsp;<a href="https://intranet.alxswe.com/rltoken/WlR0rYnv76JgX8Q-ikTqIw" title="it costs the company $2M" target="_blank">it costs the company $2M</a>. Yet, application servers often need to restart to update with the new version of the code or new configuration, when doing this operation, an application server cannot serve traffic, which meant downtime.</p>
            <p>To avoid this; application servers are designed with a master/workers infrastructure. The master is in charge of:</p>
            <ul>
                <li>Receiving requests</li>
                <li>Managing workers (starting, stopping)</li>
                <li>Distributing requests to workers</li>
            </ul>
            <p>Workers are the actual ones processing the query by generation dynamic content by processing the application code.</p>
            <p>To update an application without downtime, the master will proceed with a progressive rollout of the update. It will gracefully shut down some workers ( meaning that it will tell workers to finish processing the request they are working on, but will not send them new requests, once the worker is done, it&rsquo;s will be shutdown) and start new ones with the new application code or configuration, then move on to the other old workers until it has renewed the whole pool.</p>
            <p>Write a simple Bash script to reload Gunicorn in a graceful way.</p>
            <p>Example:</p>
            <pre><code>sylvain@ubuntu$ ps auxf | grep gunicorn
vagrant   9376  2.2  3.6  58068 18320 pts/3    S+   19:25   0:00  |   \_ /home/vagrant/AirBnB_clone_v4/bin/python3 /home/vagrant/AirBnB_clone_v4/bin/gunicorn --bind 0.0.0.0:8001 --workers 4 web_flask.0-hello_route:app
vagrant   9379  2.6  4.6  82800 23116 pts/3    S+   19:25   0:00  |       \_ /home/vagrant/AirBnB_clone_v4/bin/python3 /home/vagrant/AirBnB_clone_v4/bin/gunicorn --bind 0.0.0.0:8001 --workers 4 web_flask.0-hello_route:app
vagrant   9380  2.6  4.6  82804 23120 pts/3    S+   19:25   0:00  |       \_ /home/vagrant/AirBnB_clone_v4/bin/python3 /home/vagrant/AirBnB_clone_v4/bin/gunicorn --bind 0.0.0.0:8001 --workers 4 web_flask.0-hello_route:app
vagrant   9381  2.4  4.6  82808 23128 pts/3    S+   19:25   0:00  |       \_ /home/vagrant/AirBnB_clone_v4/bin/python3 /home/vagrant/AirBnB_clone_v4/bin/gunicorn --bind 0.0.0.0:8001 --workers 4 web_flask.0-hello_route:app
vagrant   9383  2.4  4.6  82816 23136 pts/3    S+   19:25   0:00  |       \_ /home/vagrant/AirBnB_clone_v4/bin/python3 /home/vagrant/AirBnB_clone_v4/bin/gunicorn --bind 0.0.0.0:8001 --workers 4 web_flask.0-hello_route:app
vagrant   9388  0.0  0.1  10460   940 pts/2    S+   19:25   0:00      \_ grep --color=auto gunicorn
sylvain@ubuntu$ ./4-reload_gunicorn_no_downtime
sylvain@ubuntu$ ps auxf | grep gunicorn
vagrant   9376  1.0  3.6  58068 18368 pts/3    S+   19:25   0:00  |   \_ /home/vagrant/AirBnB_clone_v4/bin/python3 /home/vagrant/AirBnB_clone_v4/bin/gunicorn --bind 0.0.0.0:8001 --workers 4 web_flask.0-hello_route:app
vagrant   9393  6.5  4.6  82832 23168 pts/3    S+   19:25   0:00  |       \_ /home/vagrant/AirBnB_clone_v4/bin/python3 /home/vagrant/AirBnB_clone_v4/bin/gunicorn --bind 0.0.0.0:8001 --workers 4 web_flask.0-hello_route:app
vagrant   9394  6.5  4.6  82832 23172 pts/3    S+   19:25   0:00  |       \_ /home/vagrant/AirBnB_clone_v4/bin/python3 /home/vagrant/AirBnB_clone_v4/bin/gunicorn --bind 0.0.0.0:8001 --workers 4 web_flask.0-hello_route:app
vagrant   9395  6.0  4.6  82840 23180 pts/3    S+   19:25   0:00  |       \_ /home/vagrant/AirBnB_clone_v4/bin/python3 /home/vagrant/AirBnB_clone_v4/bin/gunicorn --bind 0.0.0.0:8001 --workers 4 web_flask.0-hello_route:app
vagrant   9396  7.0  4.6  82844 23188 pts/3    S+   19:25   0:00  |       \_ /home/vagrant/AirBnB_clone_v4/bin/python3 /home/vagrant/AirBnB_clone_v4/bin/gunicorn --bind 0.0.0.0:8001 --workers 4 web_flask.0-hello_route:app
vagrant   9402  0.0  0.1  10460   936 pts/2    S+   19:25   0:00      \_ grep --color=auto gunicorn
sylvain@ubuntu$
</code></pre>
            <p>In this example, you can see that my Bash script tells the master Gunicorn renewed all the workers.</p>
            <p>For testing it, please use the command&nbsp;<code>$ sudo reboot</code> to reboot your server (not&nbsp;<code>shutdown</code>!!)</p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x1A-application_server</code></li>
                    <li>File:&nbsp;<code>4-reload_gunicorn_no_downtime</code></li>
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
