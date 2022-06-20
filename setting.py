class Settings:
    """存储游戏中所有设置类"""

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 0.5

        # 子弹设置
        self.bullet_speed = 0.6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_speed = 0.1
        self.fleet_drop_speed = 10
        # 1右移动 -1左移
        self.fleet_direction = 1