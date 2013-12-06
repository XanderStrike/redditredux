% rebase('base', title="Topics | Link Sharer Deluxueu")
<a href="/" class='pull-right'>back</a>
<legend>{{topic}}</legend>

Top rated links:
<ul>
  % for link in links:
    {{link[0]}} <a href="{{link[1]}}">{{link[2]}}</a> <a href="/t/{{topic}}/{{link[3]}}">-c-</a><br>
  % end
</ul>

