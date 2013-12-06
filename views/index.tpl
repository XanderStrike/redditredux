% rebase('base', title="Topics | Link Sharer Deluxueu")
<ul class="nav nav-tabs">
  <li><a href="/top">Votes</a></li>
  <li><a href="/sub">Subscribers</a></li>
  <li><a href="/pop">Links</a></li>
</ul>

<p>{{desc}}</p>
<ul>
  % for topic in topics:
    <li><a href="/t/{{topic[1]}}">{{topic[1]}}</a> ({{topic[0]}})</li>
  % end
</ul>
