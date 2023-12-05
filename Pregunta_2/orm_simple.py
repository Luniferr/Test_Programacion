""" Código que implementa una posible solución para un ORM, creando una clase llamada Book que interactúa con la base de datos mediante la clase SQL"""

class SQL:
    """Clase SQL que se encarga de la comunicación y funcionalidad directa con la base de datos"""    
    def create(self, table_name, *args, **kwargs):
        """Creates a new record in the table 'table_name' with the essential arguments in args and kwargs"""

    def update(self, table_name, record_id, *args, **kwargs):
        """Updates the record with id = 'record_id' in the table 'table_name' with the new args and kwargs """

    def delete(self, table_name, record_id, *args, **kwargs):
        """Deletes the record with id = 'record_id' from the table 'table_name'"""

    def list(self, table_name):
        """List all the records from the table 'table_name' """

    def retrieve(self, table_name, record_id):
        """Retrieves a single record with id = 'record_id' """


class Book:
    """Clase Book que permite crear objetos, guardarlos en la base de datos y actualizarlos. Tiene como base la clase llamada SQL"""    
    TABLE_NAME = 'books'

    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

    def save(self):
        """Guarda el objeto book en la base de datos"""
        SQL().create(Book.TABLE_NAME, title=self.title, author=self.author, published_year=self.published_year)

    def update(self, record_id):
        """Actualiza el objeto book en la base de datos"""
        SQL().update(Book.TABLE_NAME, record_id, title=self.title, author=self.author, published_year=self.published_year)

    @staticmethod
    def delete(record_id):
        """Elimina el objeto book en la base de datos"""
        SQL().delete(Book.TABLE_NAME, record_id)

    @staticmethod
    def list():
        """Lista todos los objetos book de la base de datos"""
        return SQL().list(Book.TABLE_NAME)

    @staticmethod
    def retrieve(record_id):
        """Recupera un objeto book único de la base de datos"""
        return SQL().retrieve(Book.TABLE_NAME, record_id)


