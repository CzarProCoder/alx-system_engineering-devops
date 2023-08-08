<h1>0x16. API advanced</h1>
<div>
    <div>PythonScriptingBack-endAPI</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Tim Britton - Cohort #1</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Project will start&nbsp;<span title="">Aug 8, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Aug 9, 2023 6:00 AM</span></li>
        <li>&nbsp;Checker&nbsp;will be&nbsp;released at&nbsp;<span title="">Aug 8, 2023 12:00 PM</span></li>
        <li>&nbsp;An auto review will be launched at the deadline</li>
    </ul>
</div>
<div>
    <div>
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/314/WIxXad8.png" alt=""></p>
        <h2>Background Context</h2>
        <p>Questions involving APIs are common for interviews. Sometimes they&rsquo;re as simple as &lsquo;write a Python script that queries a given endpoint&rsquo;, sometimes they require you to use recursive functions and format/sort the results.</p>
        <p>A great API to use for some practice is the Reddit API. There&rsquo;s a lot of endpoints available, many that don&rsquo;t require any form of authentication, and there&rsquo;s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.</p>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA" title="Reddit API Documentation" target="_blank">Reddit API Documentation</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/luFn_zrgmAQ0OAO_PEI9bA" title="Query String" target="_blank">Query String</a></li>
        </ul>
        <h2>Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/uDfkZ_HQ_YnelvPnhnBOnw" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
        <h3>General</h3>
        <ul>
            <li>How to read API documentation to find the endpoints you&rsquo;re looking for</li>
            <li>How to use an API with pagination</li>
            <li>How to parse JSON results from an API</li>
            <li>How to make a recursive API call</li>
            <li>How to sort a dictionary by value</li>
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
            <li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using&nbsp;<code>python3</code> (version 3.4.3)</li>
            <li>All your files should end with a new line</li>
            <li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
            <li>Libraries imported in your Python files must be organized in alphabetical order</li>
            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>Your code should use the&nbsp;<code>PEP 8</code> style</li>
            <li>All your files must be executable</li>
            <li>The length of your files will be tested using&nbsp;<code>wc</code></li>
            <li>All your modules should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code>)</li>
            <li>You must use the Requests module for sending HTTP requests to the Reddit API</li>
        </ul>
    </div>
</div>
<h2>Tasks</h2>
<div>
    <div>
        <div>
            <h3>0. How many subs?</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a function that queries the&nbsp;<a href="https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA" title="Reddit API" target="_blank">Reddit API</a> and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.</p>
            <p>Hint: No authentication is necessary for most features of the Reddit API. If you&rsquo;re getting errors related to Too Many Requests, ensure you&rsquo;re setting a custom User-Agent.</p>
            <p>Requirements:</p>
            <ul>
                <li>Prototype:&nbsp;<code>def number_of_subscribers(subreddit)</code></li>
                <li>If not a valid subreddit, return 0.</li>
                <li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
            </ul>
            <pre><code>wintermancer@lapbox ~/reddit_api/project $ cat 0-main.py
#!/usr/bin/python3
&quot;&quot;&quot;
0-main
&quot;&quot;&quot;
import sys

if __name__ == &apos;__main__&apos;:
    number_of_subscribers = __import__(&apos;0-subs&apos;).number_of_subscribers
    if len(sys.argv) &lt; 2:
        print(&quot;Please pass an argument for the subreddit to search.&quot;)
    else:
        print(&quot;{:d}&quot;.format(number_of_subscribers(sys.argv[1])))
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py programming
756024
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py this_is_a_fake_subreddit
0
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x16-api_advanced</code></li>
                    <li>File:&nbsp;<code>0-subs.py</code></li>
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
            <h3>1. Top Ten</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a function that queries the&nbsp;<a href="https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA" title="Reddit API" target="_blank">Reddit API</a> and prints the titles of the first 10 hot posts listed for a given subreddit.</p>
            <p>Requirements:</p>
            <ul>
                <li>Prototype:&nbsp;<code>def top_ten(subreddit)</code></li>
                <li>If not a valid subreddit, print None.</li>
                <li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
            </ul>
            <pre><code>wintermancer@lapbox ~/reddit_api/project $ cat 1-main.py
#!/usr/bin/python3
&quot;&quot;&quot;
1-main
&quot;&quot;&quot;
import sys

if __name__ == &apos;__main__&apos;:
    top_ten = __import__(&apos;1-top_ten&apos;).top_ten
    if len(sys.argv) &lt; 2:
        print(&quot;Please pass an argument for the subreddit to search.&quot;)
    else:
        top_ten(sys.argv[1])
wintermancer@lapbox ~/reddit_api/project $ python3 1-main.py programming
Firebase founder&apos;s response to last week&apos;s &quot;Firebase Costs increased by 7000%!&quot;
How a 64k intro is made
HTTPS on Stack Overflow: The End of a Long Road
Spend effort on your Git commits
It&apos;s a few years old, but I just discovered this incredibly impressive video of researchers reconstructing sounds from video information alone
From the D Blog: Introspection, Introspection Everywhere
Do MVC like it&rsquo;s 1979
GitHub is moving to GraphQL for v4 of their API (v3 was a REST API)
Google Bug Bounty - The 5k Error Page
PyCon 2017 Talk Videos
wintermancer@lapbox ~/reddit_api/project $ python3 1-main.py this_is_a_fake_subreddit
None
wintermancer@lapbox ~/reddit_api/project $ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x16-api_advanced</code></li>
                    <li>File:&nbsp;<code>1-top_ten.py</code></li>
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
            <h3>2. Recurse it!</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a&nbsp;<em>recursive function</em> that queries the&nbsp;<a href="https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA" title="Reddit API" target="_blank">Reddit API</a> and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.</p>
            <p>Hint: The Reddit API uses pagination for separating pages of responses.</p>
            <p>Requirements:</p>
            <ul>
                <li>Prototype:&nbsp;<code>def recurse(subreddit, hot_list=[])</code></li>
                <li>Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.</li>
                <li>If not a valid subreddit, return None.</li>
                <li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
            </ul>
            <p>Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)</p>
            <pre><code>wintermancer@lapbox ~/reddit_api/project $ cat 2-main.py
#!/usr/bin/python3
&quot;&quot;&quot;
2-main
&quot;&quot;&quot;
import sys

if __name__ == &apos;__main__&apos;:
    recurse = __import__(&apos;2-recurse&apos;).recurse
    if len(sys.argv) &lt; 2:
        print(&quot;Please pass an argument for the subreddit to search.&quot;)
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print(&quot;None&quot;)
wintermancer@lapbox ~/reddit_api/project $ python3 2-main.py programming
932
wintermancer@lapbox ~/reddit_api/project $ python3 2-main.py this_is_a_fake_subreddit
None
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x16-api_advanced</code></li>
                    <li>File:&nbsp;<code>2-recurse.py</code></li>
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
            <h3>3. Count it!</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Write a&nbsp;<em>recursive function</em> that queries the&nbsp;<a href="https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA" title="Reddit API" target="_blank">Reddit API</a>, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces.&nbsp;<code>Javascript</code> should count as&nbsp;<code>javascript</code>, but&nbsp;<code>java</code> should not).</p>
            <p>Requirements:</p>
            <ul>
                <li>Prototype:&nbsp;<code>def count_words(subreddit, word_list)</code></li>
                <li>Note: You may change the prototype, but it must be able to be called with just a subreddit supplied and a list of keywords. AKA you can add a counter or anything else, but the function must work without supplying a starting value in the main.</li>
                <li>If&nbsp;<code>word_list</code> contains the same word (case-insensitive), the final count should be the sum of each duplicate (example below with&nbsp;<code>java</code>)</li>
                <li>Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically (ascending, from A to Z). Words with no matches should be skipped and not printed. Words must be printed in lowercase.</li>
                <li>Results are based on the number of times a keyword appears, not titles it appears in.&nbsp;<code>java java java</code> counts as 3 separate occurrences of&nbsp;<code>java</code>.</li>
                <li>To make life easier,&nbsp;<code>java.</code> or&nbsp;<code>java!</code> or&nbsp;<code>java_</code> should not count as&nbsp;<code>java</code></li>
                <li>If no posts match or the subreddit is invalid, print nothing.</li>
                <li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are NOT following redirects.</li>
            </ul>
            <p>Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)</p>
            <p><strong>Disclaimer</strong>: number presented in this example&nbsp;<em>cannot be accurate now</em> - Reddit is hot articles are always changing.</p>
            <pre><code>bob@dylan $ cat 100-main.py 
#!/usr/bin/python3
&quot;&quot;&quot;
100-main
&quot;&quot;&quot;
import sys

if __name__ == &apos;__main__&apos;:
    count_words = __import__(&apos;100-count&apos;).count_words
    if len(sys.argv) &lt; 3:
        print(&quot;Usage: {} &lt;subreddit&gt; &lt;list of keywords&gt;&quot;.format(sys.argv[0]))
        print(&quot;Ex: {} programming &apos;python java javascript&apos;&quot;.format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
bob@dylan $             
bob@dylan $ python3 100-main.py programming &apos;react python java javascript scala no_results_for_this_one&apos;
java: 27
javascript: 20
python: 17
react: 17
scala: 4
bob@dylan $ python3 100-main.py programming &apos;JavA java&apos;
java: 54
bob@dylan $ python3 100-main.py not_a_valid_subreddit &apos;python java javascript scala no_results_for_this_one&apos;
bob@dylan $ python3 100-main.py not_a_valid_subreddit &apos;python java&apos;
bob@dylan $ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                    <li>Directory:&nbsp;<code>0x16-api_advanced</code></li>
                    <li>File:&nbsp;<code>100-count.py</code></li>
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
