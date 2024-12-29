# NORMAL FORMS
    makes it harder to get into an invalid state. (by removing redundant data)

1NF: has a key, NO mixed datatypes, values are atomic, order-insensitive
2NF: all keys - - -> each non-key field
3NF: ONLY (all keys -> each non-key field)                 <!-- field -x-> field --->
3.5NF: ONLY (all keys -> each field)
4NF: ONLY (a key ->> field)
5NF: each table should not be describable by joining other tables.
