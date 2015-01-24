from django.db import models

class File(models.Model):
    permalink = models.SlugField(u'Permalink', max_length=10, db_index=True)
    width = models.IntegerField(u'Width')
    height = models.IntegerField(u'Height')
    filetype = models.CharField(u'Filetype', max_length=4)
    filename = models.CharField(u'Filename', max_length=16)
    file_size = models.FloatField(u'File Size')
    added = models.DateTimeField(u'Added', auto_now_add=True)
    comment = models.TextField(u'Comment')
    
    #def __unicode__(self):
    #    return self.title
        
    @models.permalink
    def get_absolute_url(self):
        return ('file.views.view_file', (), {'permalink': self.permalink,})