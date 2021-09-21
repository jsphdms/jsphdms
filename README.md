## Hi there 👋

My name is Joe and this is my website.

Read [about me](./about.html) or read some of my posts:

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
