from django.db import models

class Gamsung(models.Model):
    subject = models.CharField(max_length=50, verbose_name='제목')
    contents = models.TextField(verbose_name='컨텐츠내용')
    photo = models.ImageField(blank=True, upload_to='')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='생성일자')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='업데이트일자')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')

    class Meta:
        ordering = ['-id']

    # JAVA 의 toString 과 유사한 __str__
    def __str__(self):
        return f"[{self.id}]{self.subject}"

    #== 커스텀 model 펑션의 구현 모델단에서 처리하기 
    #== 현재는 어드민 단에 해당 내용이 구현되어있음. 차이는 admin 에서는 post 인자를 통해 데이터 넘어온다는것

    # def contents_abbr(Gamsung):
    #     abbr_contents = Gamsung.contents[0:35]
    #     if len(Gamsung.contents) > 35:
    #         return abbr_contents + ' ...'
    #     else : 
    #         return abbr_contents    

    # contents_abbr.short_description = '컨텐츠 요약'