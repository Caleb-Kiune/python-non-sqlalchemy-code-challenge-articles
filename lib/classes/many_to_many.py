class Article:
    all = []

    def __init__(self, author, magazine, title):
        if isinstance(author,Author) and isinstance(magazine,Magazine):

            self.__author = author
            self.__magazine = magazine
            author._articles.append(self)
            magazine._articles.append(self)
            Article.all.append(self)
        else:
            raise ValueError('Invalid author or magazine')
        
        if isinstance(title,str) and 5 <= len(title) <= 50:
            self.__title = title
        else:
            raise ValueError('Invalid title')
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self,new_title):
        raise AttributeError('Cannot set attribute')
    
    @property
    def author(self):
        return self .__author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author,Author):
            self.__author = new_author
        else:
            raise ValueError('Invalid author')
        
    @property
    def magazine(self):
        return self.__magazine
    
    @magazine.setter
    def magazine(self,new_magazine):
        if isinstance(new_magazine,Magazine):
            self.__magazine = new_magazine
        else:raise ValueError('Invalid magazine')
    
        
class Author:
    def __init__(self, name):
        if isinstance(name,str) and len(name) > 0:
            self.__name = name
        else:
            raise ValueError('Invalid name')
        self._articles = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,new_name):
        raise AttributeError('Cannot set attribute')
    

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})
    

    def add_article(self, magazine, title):
        new_article = Article(self,magazine,title)
        return new_article

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})

class Magazine:
    def __init__(self, name, category):
        if isinstance(name,str) and 2 <= len(name) <= 16:
            self.__name = name
        else:
            raise ValueError('Invalid name')
        
        if isinstance(category,str) and len(category) > 0:
            self.__category = category
        else:
            raise ValueError('Invalid category')
        
        self._articles = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,new_name):
        if isinstance(new_name,str) and 2 <= len(new_name) <= 16:
            self.__name = new_name
        else:
            raise ValueError('Invalid name')
        
    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self,new_category):
        if isinstance(new_category,str) and len(new_category) > 0:
            self.__category = new_category
        else:
            raise ValueError('Invalid category')
        
    



        # self.name = name
        # self.category = category

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        from collections import Counter
        author_counts = Counter(article.author for article in self._articles)
        return [author for author,count in author_counts.items() if count > 2] if any (count > 2 for count in author_counts.values())else None