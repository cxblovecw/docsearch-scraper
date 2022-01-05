help = "\
Usage: make [target] \n\n\
Available targets:\n\
shell       进入pipenv环境\n\
search			开始文档搜索\n\
bootstrap   创建配置\n"

shell:
	pipenv shell

search:
	./docsearch run ./config.json

bootstrap:
	./docsearch bootstrap