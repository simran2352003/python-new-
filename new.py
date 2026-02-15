friday = {"Alice","bob","charlie"}
saturday = {"charlie","david","Eve"}
all_guests = friday.union(saturday)
print(all_guests)

data = [1,2,2,3,4,4,4,5]
data_set = set(data)
data_set.add(6)
print(data_set)



#the liberary audit
liberary_books = {"hobbit","1984","gatsby","odyssey","hamlet"}
checked_out = {"1984","hamlet"}
available_books = liberary_books - checked_out
print("available books:", available_books)
if "preschool"not in liberary_books:
 liberary_books.add("preschool")
print("updated liberary books:",liberary_books)

#permission checker
user_permission = {"read","write"}
admin_reqs = {"read","write","execute"}
has_access = admin_reqs.issubset(user_permission)
print("user has full admin access:",has_access)
missing_permissions = admin_reqs - user_permission
print("missing permissions:",missing_permissions)


#log analyzer program
server_logs = {
    "server1": {404,500,403},
    "server2": {500,403},
    "server3": {404,403},
    "server4": {404,500,403},
    "server5": {500}

}
required_errors = {404,500,403}
server_with_all_errors = {
    server for server,errors in server_logs.items()
    if required_errors.issubnet(errors)
}
print("servers with all errors (404,500,403):")
print(server_with_all_errors)
critical_servers = {
    server for server,errors in server_logs.items()
    if 500 in errors and 404 not in errors
}
print("critical servers (500 but not 404):")
print(critical_servers)
