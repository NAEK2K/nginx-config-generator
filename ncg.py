# config
index = input("index (default: index.html)\n$ ")
server_name = input("server_name (required)\n$ ")
root = input("root (default: /var/www/{domain})\n$ ")
save_location = input("save location (default: ./nginx.config)\n$ ")

# build the config
nginx_config = "index {};\n".format(index if index else "index.html")
nginx_config += "server {\n"
nginx_config += "    server_name {};\n".format(server_name)
nginx_config += "    root {};\n".format(
    root if root else "/var/www/{}".format(server_name.split(" ")[0].lstrip("www."))
)
nginx_config += "}"

# write the config
open(save_location if save_location else "nginx.config", "w+").write(nginx_config)
