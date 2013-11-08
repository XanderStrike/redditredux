% rebase('base', title="Topics | Link Sharer Deluxueu")
<legend>{{link[1]}}</legend>

<a href="{{link[0]}}">{{link[0]}}</a>

<p>{{link[2]}}</p>

Comments:
<table>
  <tr><th>User</th><th>Comment</th></tr>
  % for c in comment:
    <tr><td>{{c[0]}}</td><td>{{c[1]}}</td></tr>
  % end
</table>