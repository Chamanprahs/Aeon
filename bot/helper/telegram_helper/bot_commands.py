from bot import CMD_SUFFIX as i

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'mirror{i}', f'm{i}']
        self.YtdlCommand = [f'ytdl{i}', f'y{i}']
        self.LeechCommand = [f'leech{i}', f'l{i}']
        self.YtdlLeechCommand = [f'ytdlleech{i}', f'yl{i}']
        self.CloneCommand = [f'clone{i}', f'c{i}']
        self.CountCommand = f'count{i}'
        self.DeleteCommand = f'del{i}'
        self.StopAllCommand = [f'stopall{i}', 'stopallbot']
        self.ListCommand = f'list{i}'
        self.SearchCommand = f'search{i}'
        self.StatusCommand = [f'status{i}', 'statusall', f's{i}']
        self.UsersCommand = f'users{i}'
        self.AuthorizeCommand = [f'authorize{i}',f'a{i}']
        self.UnAuthorizeCommand = [f'unauthorize{i}',f'ua{i}']
        self.AddSudoCommand = f'addsudo{i}'
        self.RmSudoCommand = f'rmsudo{i}'
        self.PingCommand = ['ping',f'p{i}']
        self.RestartCommand = [f'restart{i}', 'restartall', f'r{i}']
        self.StatsCommand = [f'stats{i}', 'statsall']
        self.HelpCommand = f'help{i}'
        self.LogCommand = f'log{i}'
        self.ShellCommand = f'shell{i}'
        self.EvalCommand = f'eval{i}'
        self.ExecCommand = f'exec{i}'
        self.BotSetCommand = [f'botsettings{i}', f'bs{i}']
        self.UserSetCommand = [f'settings{i}', f'us{i}']
        self.SpeedCommand = f'speedtest{i}'
        self.AddImageCommand = f'addimg{i}'
        self.ImagesCommand = f'images{i}'
        self.MediaInfoCommand = f'mediainfo{i}'
        self.BroadcastCommand = [f'broadcast{i}', 'broadcastall',f'b{i}']

BotCommands = _BotCommands()
