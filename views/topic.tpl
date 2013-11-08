% rebase('base', title="Topics | Link Sharer Deluxueu")
<legend>{{topic}}</legend>

Top rated links:
<ul>
  % for link in links:
    {{link[0]}} <a href="{{link[1]}}">{{link[2]}}</a> <a href="/t/{{topic}}/{{link[1]}}">-c-</a><br>
  % end
</ul>

<a href="/">back</a>