from django import template

register = template.Library()

@register.filter
def hashtag_link(post):
    content = post.content   # '#강아지 #고양이'
    hashtags = post.hashtags.all()    # <queryset [hashtag1, hashtag6]>
    
    for hashtag in hashtags:
        # #하이 => <a href="{% url 'posts:hashtag' hashtag.id %}">#하이</a>
        # hashtag.content => <a href="{% url 'posts:hashtag' hashtag.id %}"> hashtag.content </a>
        
        content = content.replace(f"{hashtag.content}", f"<a href='/posts/hashtag/{hashtag.id}/'> {hashtag.content} </a>" )
    
    return content
    