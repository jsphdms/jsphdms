Read [about me](./about) or browse some posts:

{% for post in site.posts %}
  <a href="{{ post.url }}">{{ post.title }}</a>
{% endfor %}
