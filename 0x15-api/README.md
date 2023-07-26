<main>
    <div><br></div>
    <article>
        <div>
            <div>
                <h1>0x15. API</h1>
                <div>
                    <div>PythonScriptingBack-endAPI</div>
                </div>
                <div>
                    <ul>
                        <li>&nbsp;By:&nbsp;Sylvain Kalache, co-founder at Holberton School</li>
                        <li>&nbsp;Weight:&nbsp;1</li>
                        <li>&nbsp;Project will start&nbsp;<span title="">Jul 24, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Jul 25, 2023 6:00 AM</span></li>
                        <li>&nbsp;Checker&nbsp;was&nbsp;released at&nbsp;<span title="">Jul 24, 2023 12:00 PM</span></li>
                        <li>&nbsp;An auto review will be launched at the deadline</li>
                    </ul>
                </div>
                <div>
                    <div>
                        <h2>Background Context</h2>
                        <p><a href="https://youtu.be/-2kyU6-j8ZQ" target="_blank"><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/897638f42eb1bad6605d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230724T125240Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2da601ba6a8e61873ff5d73bf96038066c85d5d336fd602b85acc74a193cc248" alt=""></a></p>
                        <p>Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.</p>
                        <p>One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them &ndash; access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.</p>
                        <p>This is a perfect example of a task that is not suited for Bash scripting, so let&rsquo;s build Python scripts.</p>
                        <h2>Resources</h2>
                        <p><strong>Read or watch</strong>:</p>
                        <ul>
                            <li><a href="https://intranet.alxswe.com/rltoken/KMFzqRAqedMf7AHHBD_43g" title="Friends don't let friends program in shell script" target="_blank">Friends don&rsquo;t let friends program in shell script</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/zeBO6_RNTlwaotyRRNAzoQ" title="What is an API" target="_blank">What is an API</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/bf09Qp6QY44CANLzxxRbPA" title="What is an API? In English, please" target="_blank">What is an API? In English, please</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/fA164QWEnZxaSngBD3EPRQ" title="What is a REST API" target="_blank">What is a REST API</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/n4h77IbBuDxTE3bhes_AyQ" title="What are microservices" target="_blank">What are microservices</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/b7V1ROY6kSRxDDKnsJoqxg" title="PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry" target="_blank">PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry</a></li>
                        </ul>
                        <h2>Learning Objectives</h2>
                        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/03Evn5VsICwJUAiTdu0zHA" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
                        <h3>General</h3>
                        <ul>
                            <li>What Bash scripting should not be used for</li>
                            <li>What is an API</li>
                            <li>What is a REST API</li>
                            <li>What are microservices</li>
                            <li>What is the CSV format</li>
                            <li>What is the JSON format</li>
                            <li>Pythonic Package and module name style</li>
                            <li>Pythonic Class name style</li>
                            <li>Pythonic Variable name style</li>
                            <li>Pythonic Function name style</li>
                            <li>Pythonic Constant name style</li>
                            <li>Significance of CapWords or CamelCase in Python</li>
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
                            <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
                            <li>All your files should end with a new line</li>
                            <li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
                            <li><strong>Libraries imported in your Python files must be organized in alphabetical order</strong></li>
                            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
                            <li>Your code should use the pycodestyle (version&nbsp;<code>2.8.*</code>)</li>
                            <li>All your files must be executable</li>
                            <li>The length of your files will be tested using&nbsp;<code>wc</code></li>
                            <li>All your modules should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code>)</li>
                            <li>You must use&nbsp;<a href="https://intranet.alxswe.com/rltoken/CNqOWPW6mdYuK7Ak-f2KHQ" title="get" target="_blank">get</a> to access to dictionary value by key (it won&rsquo;t throw an exception if the key doesn&rsquo;t exist in the dictionary)</li>
                            <li>Your code should not be executed when imported (by using&nbsp;<code>if __name__ == &quot;__main__&quot;:</code>)</li>
                        </ul>
                    </div>
                </div>
                <h2>Tasks</h2>
                <div>
                    <div>
                        <div>
                            <h3>0. Gather data from an API</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <p>Write a Python script that, using this&nbsp;<a href="https://intranet.alxswe.com/rltoken/7cr7aLYdaWAZWBKrBKS12A" title="REST API" target="_blank">REST API</a>, for a given employee ID, returns information about his/her TODO list progress.</p>
                            <p>Requirements:</p>
                            <ul>
                                <li>You must use&nbsp;<code>urllib</code> or&nbsp;<code>requests</code> module</li>
                                <li>The script must accept an integer as a parameter, which is the employee ID</li>
                                <li>The script must display on the standard output the employee TODO list progress in this exact format:<ul>
                                        <li>First line:&nbsp;<code>Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):</code>
                                            <ul>
                                                <li><code>EMPLOYEE_NAME</code>: name of the employee</li>
                                                <li><code>NUMBER_OF_DONE_TASKS</code>: number of completed tasks</li>
                                                <li><code>TOTAL_NUMBER_OF_TASKS</code>: total number of tasks, which is the sum of completed and non-completed tasks</li>
                                            </ul>
                                        </li>
                                        <li>Second and N next lines display the title of completed tasks:&nbsp;<code>TASK_TITLE</code> (with 1 tabulation and 1 space before the&nbsp;<code>TASK_TITLE</code>)</li>
                                    </ul>
                                </li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4
Employee Patricia Lebsack is done with tasks(6/20):
     odit optio omnis qui sunt
     doloremque aut dolores quidem fuga qui nulla
     sint amet quia totam corporis qui exercitationem commodi
     sequi dolorem sed
     eum ipsa maxime ut
     tempore molestias dolores rerum sequi voluptates ipsum consequatur
sylvain@ubuntu$
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4 | tr &quot; &quot; &quot;S&quot; | tr &quot;\t&quot; &quot;T&quot; 
EmployeeSPatriciaSLebsackSisSdoneSwithStasks(6/20):
TSoditSoptioSomnisSquiSsunt
TSdoloremqueSautSdoloresSquidemSfugaSquiSnulla
TSsintSametSquiaStotamScorporisSquiSexercitationemScommodi
TSsequiSdoloremSsed
TSeumSipsaSmaximeSut
TStemporeSmolestiasSdoloresSrerumSsequiSvoluptatesSipsumSconsequatur
sylvain@ubuntu$
</code></pre>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x15-api</code></li>
                                    <li>File:&nbsp;<code>0-gather_data_from_an_API.py</code></li>
                                </ul>
                            </div>
                        </div>
                        <div>
                            <div>
                                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                                <div><br></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <div>
                        <div>
                            <h3>1. Export to CSV</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <p>Using what you did in the task #0, extend your Python script to export data in the CSV format.</p>
                            <p>Requirements:</p>
                            <ul>
                                <li>Records all tasks that are owned by this employee</li>
                                <li>Format must be:&nbsp;<code>&quot;USER_ID&quot;,&quot;USERNAME&quot;,&quot;TASK_COMPLETED_STATUS&quot;,&quot;TASK_TITLE&quot;</code></li>
                                <li>File name must be:&nbsp;<code>USER_ID.csv</code></li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>sylvain@ubuntu$ python3 1-export_to_CSV.py 2
sylvain@ubuntu$ cat 2.csv
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;suscipit repellat esse quibusdam voluptatem incidunt&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;distinctio vitae autem nihil ut molestias quo&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;et itaque necessitatibus maxime molestiae qui quas velit&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;adipisci non ad dicta qui amet quaerat doloribus ea&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;voluptas quo tenetur perspiciatis explicabo natus&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;aliquam aut quasi&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;veritatis pariatur delectus&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;nesciunt totam sit blanditiis sit&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;laborum aut in quam&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;repudiandae totam in est sint facere fuga&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;earum doloribus ea doloremque quis&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;sint sit aut vero&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;porro aut necessitatibus eaque distinctio&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;repellendus veritatis molestias dicta incidunt&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;excepturi deleniti adipisci voluptatem et neque optio illum ad&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;sunt cum tempora&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;totam quia non&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;doloremque quibusdam asperiores libero corrupti illum qui omnis&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;totam atque quo nesciunt&quot;
sylvain@ubuntu$
</code></pre>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x15-api</code></li>
                                    <li>File:&nbsp;<code>1-export_to_CSV.py</code></li>
                                </ul>
                            </div>
                        </div>
                        <div>
                            <div>
                                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                                <div><br></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <div>
                        <div>
                            <h3>2. Export to JSON</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p>
                            <p>Requirements:</p>
                            <ul>
                                <li>Records all tasks that are owned by this employee</li>
                                <li>Format must be:&nbsp;<code>{ &quot;USER_ID&quot;: [{&quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS, &quot;username&quot;: &quot;USERNAME&quot;}, {&quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS, &quot;username&quot;: &quot;USERNAME&quot;}, ... ]}</code></li>
                                <li>File name must be:&nbsp;<code>USER_ID.json</code></li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>sylvain@ubuntu$ python3 2-export_to_JSON.py 2
sylvain@ubuntu$ cat 2.json
{&quot;2&quot;: [{&quot;task&quot;: &quot;suscipit repellat esse quibusdam voluptatem incidunt&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;distinctio vitae autem nihil ut molestias quo&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;et itaque necessitatibus maxime molestiae qui quas velit&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;adipisci non ad dicta qui amet quaerat doloribus ea&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;voluptas quo tenetur perspiciatis explicabo natus&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;aliquam aut quasi&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;veritatis pariatur delectus&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;nesciunt totam sit blanditiis sit&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;laborum aut in quam&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;repudiandae totam in est sint facere fuga&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;earum doloribus ea doloremque quis&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;sint sit aut vero&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;porro aut necessitatibus eaque distinctio&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;repellendus veritatis molestias dicta incidunt&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;excepturi deleniti adipisci voluptatem et neque optio illum ad&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;sunt cum tempora&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;totam quia non&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;doloremque quibusdam asperiores libero corrupti illum qui omnis&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;totam atque quo nesciunt&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}]}sylvain@ubuntu$
</code></pre>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x15-api</code></li>
                                    <li>File:&nbsp;<code>2-export_to_JSON.py</code></li>
                                </ul>
                            </div>
                        </div>
                        <div>
                            <div>
                                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                                <div><br></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <div>
                        <div>
                            <h3>3. Dictionary of list of dictionaries</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p>
                            <p>Requirements:</p>
                            <ul>
                                <li>Records all tasks from all employees</li>
                                <li>Format must be:&nbsp;<code>{ &quot;USER_ID&quot;: [ {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, ... ], &quot;USER_ID&quot;: [ {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, ... ]}</code></li>
                                <li>File name must be:&nbsp;<code>todo_all_employees.json</code></li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>sylvain@ubuntu$ python3 3-dictionary_of_list_of_dictionaries.py
sylvain@ubuntu$ cat todo_all_employees.json
{&quot;1&quot;: [{&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;delectus aut autem&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;quis ut nam facilis et officia qui&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;fugiat veniam minus&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;et porro tempora&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;laboriosam mollitia et enim quasi adipisci quia provident illum&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;qui ullam ratione quibusdam voluptatem quia omnis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;illo expedita consequatur quia in&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;quo adipisci enim quam ut ab&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;molestiae perspiciatis ipsa&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;illo est ratione doloremque quia maiores aut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;vero rerum temporibus dolor&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;ipsa repellendus fugit nisi&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;et doloremque nulla&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;repellendus sunt dolores architecto voluptatum&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;ab voluptatum amet voluptas&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;accusamus eos facilis sint et aut voluptatem&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;quo laboriosam deleniti aut qui&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;dolorum est consequatur ea mollitia in culpa&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;molestiae ipsa aut voluptatibus pariatur dolor nihil&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;ullam nobis libero sapiente ad optio sint&quot;, &quot;completed&quot;: true}], &quot;2&quot;: [{&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;suscipit repellat esse quibusdam voluptatem incidunt&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;distinctio vitae autem nihil ut molestias quo&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;et itaque necessitatibus maxime molestiae qui quas velit&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;adipisci non ad dicta qui amet quaerat doloribus ea&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;voluptas quo tenetur perspiciatis explicabo natus&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;aliquam aut quasi&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;veritatis pariatur delectus&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;nesciunt totam sit blanditiis sit&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;laborum aut in quam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;repudiandae totam in est sint facere fuga&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;earum doloribus ea doloremque quis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;sint sit aut vero&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;porro aut necessitatibus eaque distinctio&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;repellendus veritatis molestias dicta incidunt&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;excepturi deleniti adipisci voluptatem et neque optio illum ad&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;sunt cum tempora&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;totam quia non&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;doloremque quibusdam asperiores libero corrupti illum qui omnis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;totam atque quo nesciunt&quot;, &quot;completed&quot;: true}], &quot;3&quot;: [{&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;aliquid amet impedit consequatur aspernatur placeat eaque fugiat suscipit&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;rerum perferendis error quia ut eveniet&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;tempore ut sint quis recusandae&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;cum debitis quis accusamus doloremque ipsa natus sapiente omnis&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;velit soluta adipisci molestias reiciendis harum&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;vel voluptatem repellat nihil placeat corporis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;nam qui rerum fugiat accusamus&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;sit reprehenderit omnis quia&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;ut necessitatibus aut maiores debitis officia blanditiis velit et&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;cupiditate necessitatibus ullam aut quis dolor voluptate&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;distinctio exercitationem ab doloribus&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;nesciunt dolorum quis recusandae ad pariatur ratione&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;qui labore est occaecati recusandae aliquid quam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;quis et est ut voluptate quam dolor&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;voluptatum omnis minima qui occaecati provident nulla voluptatem ratione&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;deleniti ea temporibus enim&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;pariatur et magnam ea doloribus similique voluptatem rerum quia&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;est dicta totam qui explicabo doloribus qui dignissimos&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;perspiciatis velit id laborum placeat iusto et aliquam odio&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;et sequi qui architecto ut adipisci&quot;, &quot;completed&quot;: true}], &quot;4&quot;: [{&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;odit optio omnis qui sunt&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;et placeat et tempore aspernatur sint numquam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;doloremque aut dolores quidem fuga qui nulla&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;voluptas consequatur qui ut quia magnam nemo esse&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;fugiat pariatur ratione ut asperiores necessitatibus magni&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;rerum eum molestias autem voluptatum sit optio&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;quia voluptatibus voluptatem quos similique maiores repellat&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;aut id perspiciatis voluptatem iusto&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;doloribus sint dolorum ab adipisci itaque dignissimos aliquam suscipit&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;ut sequi accusantium et mollitia delectus sunt&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;aut velit saepe ullam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;praesentium facilis facere quis harum voluptatibus voluptatem eum&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;sint amet quia totam corporis qui exercitationem commodi&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;expedita tempore nobis eveniet laborum maiores&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;occaecati adipisci est possimus totam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;sequi dolorem sed&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;maiores aut nesciunt delectus exercitationem vel assumenda eligendi at&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;reiciendis est magnam amet nemo iste recusandae impedit quaerat&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;eum ipsa maxime ut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;tempore molestias dolores rerum sequi voluptates ipsum consequatur&quot;, &quot;completed&quot;: true}], &quot;5&quot;: [{&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;suscipit qui totam&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;voluptates eum voluptas et dicta&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;quidem at rerum quis ex aut sit quam&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;sunt veritatis ut voluptate&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;et quia ad iste a&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;incidunt ut saepe autem&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;laudantium quae eligendi consequatur quia et vero autem&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;vitae aut excepturi laboriosam sint aliquam et et accusantium&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;sequi ut omnis et&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;molestiae nisi accusantium tenetur dolorem et&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;nulla quis consequatur saepe qui id expedita&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;in omnis laboriosam&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;odio iure consequatur molestiae quibusdam necessitatibus quia sint&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;facilis modi saepe mollitia&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;vel nihil et molestiae iusto assumenda nemo quo ut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;nobis suscipit ducimus enim asperiores voluptas&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;dolorum laboriosam eos qui iure aliquam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;debitis accusantium ut quo facilis nihil quis sapiente necessitatibus&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;neque voluptates ratione&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;excepturi a et neque qui expedita vel voluptate&quot;, &quot;completed&quot;: false}], &quot;6&quot;: [{&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;explicabo enim cumque porro aperiam occaecati minima&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;sed ab consequatur&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;non sunt delectus illo nulla tenetur enim omnis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;excepturi non laudantium quo&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;totam quia dolorem et illum repellat voluptas optio&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;ad illo quis voluptatem temporibus&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;praesentium facilis omnis laudantium fugit ad iusto nihil nesciunt&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;a eos eaque nihil et exercitationem incidunt delectus&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;autem temporibus harum quisquam in culpa&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;aut aut ea corporis&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;magni accusantium labore et id quis provident&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;consectetur impedit quisquam qui deserunt non rerum consequuntur eius&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;quia atque aliquam sunt impedit voluptatum rerum assumenda nisi&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;cupiditate quos possimus corporis quisquam exercitationem beatae&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;sed et ea eum&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;ipsa dolores vel facilis ut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;sequi quae est et qui qui eveniet asperiores&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;quia modi consequatur vero fugiat&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;corporis ducimus ea perspiciatis iste&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;dolorem laboriosam vel voluptas et aliquam quasi&quot;, &quot;completed&quot;: false}], &quot;7&quot;: [{&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;inventore aut nihil minima laudantium hic qui omnis&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;provident aut nobis culpa&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;esse et quis iste est earum aut impedit&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;qui consectetur id&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;aut quasi autem iste tempore illum possimus&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;ut asperiores perspiciatis veniam ipsum rerum saepe&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;voluptatem libero consectetur rerum ut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;eius omnis est qui voluptatem autem&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;rerum culpa quis harum&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;nulla aliquid eveniet harum laborum libero alias ut unde&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;qui ea incidunt quis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;qui molestiae voluptatibus velit iure harum quisquam&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;et labore eos enim rerum consequatur sunt&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;molestiae doloribus et laborum quod ea&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;facere ipsa nam eum voluptates reiciendis vero qui&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;asperiores illo tempora fuga sed ut quasi adipisci&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;qui sit non&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;placeat minima consequatur rem qui ut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;consequatur doloribus id possimus voluptas a voluptatem&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;aut consectetur in blanditiis deserunt quia sed laboriosam&quot;, &quot;completed&quot;: true}], &quot;8&quot;: [{&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;explicabo consectetur debitis voluptates quas quae culpa rerum non&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;maiores accusantium architecto necessitatibus reiciendis ea aut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;eum non recusandae cupiditate animi&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;ut eum exercitationem sint&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;beatae qui ullam incidunt voluptatem non nisi aliquam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;molestiae suscipit ratione nihil odio libero impedit vero totam&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;eum itaque quod reprehenderit et facilis dolor autem ut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;esse quas et quo quasi exercitationem&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;animi voluptas quod perferendis est&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;eos amet tempore laudantium fugit a&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;accusamus adipisci dicta qui quo ea explicabo sed vero&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;odit eligendi recusandae doloremque cumque non&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;ea aperiam consequatur qui repellat eos&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;rerum non ex sapiente&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;voluptatem nobis consequatur et assumenda magnam&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;nam quia quia nulla repellat assumenda quibusdam sit nobis&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;dolorem veniam quisquam deserunt repellendus&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;debitis vitae delectus et harum accusamus aut deleniti a&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;debitis adipisci quibusdam aliquam sed dolore ea praesentium nobis&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;et praesentium aliquam est&quot;, &quot;completed&quot;: false}], &quot;9&quot;: [{&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;ex hic consequuntur earum omnis alias ut occaecati culpa&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;omnis laboriosam molestias animi sunt dolore&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;natus corrupti maxime laudantium et voluptatem laboriosam odit&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;reprehenderit quos aut aut consequatur est sed&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;fugiat perferendis sed aut quidem&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;quos quo possimus suscipit minima ut&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;et quis minus quo a asperiores molestiae&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;recusandae quia qui sunt libero&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;ea odio perferendis officiis&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;quisquam aliquam quia doloribus aut&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;fugiat aut voluptatibus corrupti deleniti velit iste odio&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;et provident amet rerum consectetur et voluptatum&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;harum ad aperiam quis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;similique aut quo&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;laudantium eius officia perferendis provident perspiciatis asperiores&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;magni soluta corrupti ut maiores rem quidem&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;et placeat temporibus voluptas est tempora quos quibusdam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;nesciunt itaque commodi tempore&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;omnis consequuntur cupiditate impedit itaque ipsam quo&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;debitis nisi et dolorem repellat et&quot;, &quot;completed&quot;: true}], &quot;10&quot;: [{&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;ut cupiditate sequi aliquam fuga maiores&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;inventore saepe cumque et aut illum enim&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;omnis nulla eum aliquam distinctio&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;molestias modi perferendis perspiciatis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;voluptates dignissimos sed doloribus animi quaerat aut&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;explicabo odio est et&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;consequuntur animi possimus&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;vel non beatae est&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;culpa eius et voluptatem et&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;accusamus sint iusto et voluptatem exercitationem&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;temporibus atque distinctio omnis eius impedit tempore molestias pariatur&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;ut quas possimus exercitationem sint voluptates&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;rerum debitis voluptatem qui eveniet tempora distinctio a&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;sed ut vero sit molestiae&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;rerum ex veniam mollitia voluptatibus pariatur&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;consequuntur aut ut fugit similique&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;dignissimos quo nobis earum saepe&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;quis eius est sint explicabo&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;numquam repellendus a magnam&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;ipsam aperiam voluptates qui&quot;, &quot;completed&quot;: false}]}sylvain@ubuntu$
</code></pre>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x15-api</code></li>
                                    <li>File:&nbsp;<code>3-dictionary_of_list_of_dictionaries.py</code></li>
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
            </div>
        </div>
    </article>
</main>
