import os
import re
from django.core.management.base import (
    BaseCommand, CommandParser
)

# https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/
class Command(BaseCommand):

    r"""React Build & Django Template Auto Edit"""
    message     = 'building js & css copy to html\n'
    file_django = './core/templates/base.html'
    file_build  = './staticfiles/index.html'

    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)

    def handle(self, *args, **options):

        # Pre Processing
        build_data    = {}
        build_targets = {'js':"/assets/",'css':"/assets/"}
        if os.path.exists(self.file_build) == False:
            self.stdout.write(f"{self.file_build} is not existed ...")
            return None

        # Process 1 : 빌드된 파일에서 필요한 정보찾기
        with open(self.file_build, 'r') as f:
            texts = f.readlines()

        tokenizer = re.compile(r'assets/[tjscx]+/[A-z0-9\-\.]+.[tjscx]+')
        for text in texts:
            for file_type, hint in build_targets.items():
                if (text.find(hint) != -1) & (text.find(f".{file_type}") != -1):
                    text = "".join(tokenizer.findall(text))
                    build_data[file_type] = text

        # Process 2 : Django Template 에 추출한 내용 입력하기
        with open(self.file_django, 'r') as f:
            texts = f.readlines()

        result_list  = []
        result_text  = self.message
        for text in texts:
            for _type in ['css', 'js']:
                if (text.find("{% static") != -1) & (text.find(f".{_type}") != -1):
                    check = "".join(re.findall(r'assets/[jstcx]+/[.A-z0-9\-\.]+', text))
                    text  = re.sub(check, build_data[_type], text)
                    result_text += f"{check} => {build_data[_type]}\n"
            result_list.append(text)

        # 결과값 저장하기 & 결과 메세지 출력
        with open(self.file_django, 'w') as f:
            f.write("".join(result_list))
        self.stdout.write(result_text)