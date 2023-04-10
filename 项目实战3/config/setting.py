import pathlib


class Config:
    # 域名
    admin_host = 'http://mall.lemonban.com:8108'

    # 获取当前文件路径
    current_path = pathlib.Path(__file__).absolute()
    # 项目的根目录
    root_dir = current_path.parent.parent
    # 测试数据存储目录
    data_dir = root_dir / 'data'
    # cases 文件
    case_file = data_dir / 'cases.xlsx'

    # 图鉴用户
    tujian_uname = 'simple'
    tujian_passwd = 'yuan5311645'

    # 登录用户名密码
    admin_username = 'student'
    admin_passwd = '123456a'


if __name__ == '__main__':
    print(Config.current_path)
