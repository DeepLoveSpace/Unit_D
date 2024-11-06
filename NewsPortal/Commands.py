py manage.py shell
from news.models import *

1.
u1=User.objects.create_user('Денис')
u2=User.objects.create_user('Дарья')

2
a1=Author.objects.create(user=u1)
a2=Author.objects.create(user=u2)

3
c1=Category.objects.create(name='Экономика')
c2=Category.objects.create(name='Политика')
c3=Category.objects.create(name='Спорт')
c4=Category.objects.create(name='Бизнес')

4
p1=Post.objects.create(title='Заголовок 1', text='текст статьи 1', post_type='art', author=a1)
p2=Post.objects.create(title='Заголовок 2', text='текст статьи 2', post_type='art', author=a2)
p3=Post.objects.create(title='Заголовок 3', text='текст новостей 3', post_type='new', author=a2)

5
post1=Post.objects.get(pk=1)
category1=Category.objects.get(pk=1)
category2=Category.objects.get(pk=2)
PostCategory.objects.create(post=post1, category=category1)
PostCategory.objects.create(post=post1, category=category2)

6
c1=Comment.objects.create(text='текст комментария 1', post=p1, user=a1.user)
c2=Comment.objects.create(text='текст комментария 2', post=p1, user=a2.user)
c3=Comment.objects.create(text='текст комментария 3', post=p2, user=a1.user)
c4=Comment.objects.create(text='текст комментария 4', post=p3, user=a1.user)

7
c1.like()
c2.like()
c2.like()
c2.like()
c2.like()
c2.like()
c2.like()
c2.dislike()
c2.dislike()
c1.like()
p1.like()
p1.like()
p2.dislike()

8
a1.update_rating()
a2.update_rating()

9
author_best=Author.objects.order_by('-rating').first()
author_best.user.username
author_best.rating

10
post_best=Post.objects.order_by('-rating').first()
post_best.post_time
post_best.author.user.username
post_best.rating
post_best.title
post_best.preview()

11
Comment.objects.filter(post=post_best).values('comment_time', 'user', 'rating', 'text')