Models inheritance works the same way as normal Python class inheritance works, the only difference is, whether we want the parent models to have their own table in the database or not. When the parent model tables are not created as tables it just acts as a container for common fields and methods. We will see examples to understand it in detail. There are three styles of inheritance possible in Django.

Abstract base classes: Use this when the parent class contains common fields and the parent class table is not desirable.
Multi-table inheritance: Use this when the parent class has common fields, but the parent class table also exists in the database all by itself.
Proxy models: Use this when you want to modify the behavior of the parent class, like by changing orderby or a new model manager.
