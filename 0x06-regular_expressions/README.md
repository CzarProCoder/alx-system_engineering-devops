<main>
    <div><br></div>
    <article>
        <div>
            <div>
                <h1>0x06. Regular expression</h1>
                <div>
                    <div>RegexDevOps</div>
                </div>
                <div>
                    <ul>
                        <li>&nbsp;By:&nbsp;Sylvain Kalache</li>
                        <li>&nbsp;Weight:&nbsp;1</li>
                        <li>&nbsp;Project over - took place from&nbsp;<span title="">May 3, 2023 6:00 AM</span> to&nbsp;<span title="">May 4, 2023 6:00 AM</span></li>
                        <li>&nbsp;An auto review will be launched at the deadline</li>
                    </ul>
                </div>
                <div>
                    <h4>In a nutshell&hellip;</h4>
                    <ul>
                        <li><strong>Auto QA review:</strong> 2.0/24 mandatory &amp; 0.0/9 optional</li>
                        <li><strong>Altogether:</strong>&nbsp; <strong>8.33%</strong>
                            <ul>
                                <li>Mandatory: 8.33%</li>
                                <li>Optional: 0.0%</li>
                                <li>Calculation: &nbsp;8.33% + (8.33% * 0.0%) &nbsp;== <strong>8.33%</strong></li>
                            </ul>
                        </li>
                    </ul>
                </div>
                <div>
                    <div>
                        <h3>Concepts</h3>
                    </div>
                    <div>
                        <p><em>For this project, we expect you to look at this concept:</em></p>
                        <ul>
                            <li><a href="https://intranet.alxswe.com/concepts/29">Regular Expression</a></li>
                        </ul>
                    </div>
                </div>
                <div>
                    <div>
                        <h2>Background Context</h2>
                        <p>For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.</p>
                        <p>Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the&nbsp;<code>//</code>:</p>
                        <pre><code>sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
</code></pre>
                        <h2>Resources</h2>
                        <p><strong>Read or watch</strong>:</p>
                        <ul>
                            <li><a href="https://intranet.alxswe.com/rltoken/6VeaVMaugIxcFAwA27TBdQ" title="Regular expressions - basics" target="_blank">Regular expressions - basics</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/rntjh3-3S86zt0Qy28L10w" title="Regular expressions - advanced" target="_blank">Regular expressions - advanced</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/RGkVuw1lZ_hoCCbLsiOAhg" title="Rubular is your best friend" target="_blank">Rubular is your best friend</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/Vwm8lpMUGa4x_FBtlyUQ8g" title="Use a regular expression against a problem: now you have 2 problems" target="_blank">Use a regular expression against a problem: now you have 2 problems</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/XsQ6rzS1uy-E6bnswUqIKg" title="Learn Regular Expressions with simple, interactive exercises" target="_blank">Learn Regular Expressions with simple, interactive exercises</a></li>
                        </ul>
                        <h2>Requirements</h2>
                        <h3>General</h3>
                        <ul>
                            <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
                            <li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
                            <li>All your files should end with a new line</li>
                            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
                            <li>All your Bash script files must be executable</li>
                            <li>The first line of all your Bash scripts should be exactly&nbsp;<code>#!/usr/bin/env ruby</code></li>
                            <li>All your regex must be built for the Oniguruma library</li>
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
                            <h3>0. Simply matching School</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;50.0%&nbsp;(Checks completed: 100.0%)</div>
                            </div>
                            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230508T200325Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5629655ca468290dce87833fc73cb365d46bb21ce013a1baa3bed6a54364ecd7" alt=""></p>
                            <p>Requirements:</p>
                            <ul>
                                <li>The regular expression must match&nbsp;<code>School</code></li>
                                <li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb &quot;Best School&quot; | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb &quot;School Best School&quot; | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_school.rb &quot;Grace Hopper&quot; | cat -e
$
</code></pre>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x06-regular_expressions</code></li>
                                    <li>File:&nbsp;<code>0-simply_match_school.rb</code></li>
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
                            <h3>1. Repetition Token #0</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230508T200325Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=64f275a4201387bc9f7d74cd2abe8aba09dc828010d28fe0fc73228503f9a644" alt=""></p>
                            <p>Requirements:</p>
                            <ul>
                                <li>Find the regular expression that will match the above cases</li>
                                <li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
                            </ul>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x06-regular_expressions</code></li>
                                    <li>File:&nbsp;<code>1-repetition_token_0.rb</code></li>
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
                            <h3>2. Repetition Token #1</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230508T200325Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=be245fedb04b6791952b4304e2912a346f53e987b8147ca7f153055cdf25a57b" alt=""></p>
                            <p>Requirements:</p>
                            <ul>
                                <li>Find the regular expression that will match the above cases</li>
                                <li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
                            </ul>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x06-regular_expressions</code></li>
                                    <li>File:&nbsp;<code>2-repetition_token_1.rb</code></li>
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
                            <h3>3. Repetition Token #2</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230508T200325Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a6c6b7a77cf15b426e549c1ce71a821a1a51905b5b8a1a9e69040769b62f020c" alt=""></p>
                            <p>Requirements:</p>
                            <ul>
                                <li>Find the regular expression that will match the above cases</li>
                                <li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
                            </ul>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x06-regular_expressions</code></li>
                                    <li>File:&nbsp;<code>3-repetition_token_2.rb</code></li>
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
                            <h3>4. Repetition Token #3</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230508%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230508T200325Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=62e826f565d082a9e98ed97adf5dcdc4266788cf8a227fdfdc1a40e626a885b3" alt=""></p>
                            <p>Requirements:</p>
                            <ul>
                                <li>Find the regular expression that will match the above cases</li>
                                <li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
                                <li>Your regex should not contain square brackets</li>
                            </ul>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x06-regular_expressions</code></li>
                                    <li>File:&nbsp;<code>4-repetition_token_3.rb</code></li>
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
                            <h3>5. Not quite HBTN yet</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p>Requirements:</p>
                            <ul>
                                <li>The regular expression must be exactly matching a string that starts with&nbsp;<code>h</code> ends with&nbsp;<code>n</code> and can have any single character in between</li>
                                <li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>sylvain@ubuntu$ ./5-beginning_and_end.rb &apos;hn&apos; | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb &apos;hbn&apos; | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb &apos;hbtn&apos; | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb &apos;h8n&apos; | cat -e
h8n$
sylvain@ubuntu$
$
</code></pre>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x06-regular_expressions</code></li>
                                    <li>File:&nbsp;<code>5-beginning_and_end.rb</code></li>
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
                            <h3>6. Call me maybe</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p>This task is brought to you by a professional advisor&nbsp;<a href="https://intranet.alxswe.com/rltoken/GqwvXAvTXR_JXqyTvZ4AzQ" title="Neha Jain" target="_blank">Neha Jain</a>, Senior Software Engineer at LinkedIn.</p>
                            <p>Requirement:</p>
                            <ul>
                                <li>The regular expression must match a 10 digit phone number</li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb &quot; 4155049898&quot; | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb &quot;415 504 9898&quot; | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb &quot;415-504-9898&quot; | cat -e
$
sylvain@ubuntu$
</code></pre>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x06-regular_expressions</code></li>
                                    <li>File:&nbsp;<code>6-phone_number.rb</code></li>
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
                            <h3>7. OMG WHY ARE YOU SHOUTING?</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p><img src="https://intranet.alxswe.com/images/contents/sysadmin/projects/78/shouting.jpg" alt=""></p>
                            <p>Requirement:</p>
                            <ul>
                                <li>The regular expression must be only matching: capital letters</li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb &quot;I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream&quot; | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb &quot;WHAT do you SAY?&quot; | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb &quot;cannot read you&quot; | cat -e
$
sylvain@ubuntu$
</code></pre>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x06-regular_expressions</code></li>
                                    <li>File:&nbsp;<code>7-OMG_WHY_ARE_YOU_SHOUTING.rb</code></li>
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
