class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = 'mirror', 'seed'
        self.UnzipMirrorCommand = 'unpack'
        self.TarMirrorCommand = 'tarmirror'
        self.ZipMirrorCommand = 'zipmirror'
        self.CancelMirror = 'cancel'
        self.CancelAllCommand = 'cancelall'
        self.ListCommand = 'list'
        self.StatusCommand = 'status'
        self.AuthorizedUsersCommand = 'users'
        self.AuthorizeCommand = 'auth'
        self.UnAuthorizeCommand = 'unauth'
        self.AddSudoCommand = 'sudo'
        self.RmSudoCommand = 'unsudo'
        self.PingCommand = 'ping'
        self.RestartCommand = 'restart'
        self.StatsCommand = 'stats'
        self.HelpCommand = 'help'
        self.LogCommand = 'log'
        self.SpeedCommand = 'speedtest', 'speed', 'st'
        self.CloneCommand = 'gd', 'clone'
        self.CountCommand = 'count'
        self.WatchCommand = 'watch'
        self.TarWatchCommand = 'tarwatch'
        self.ZipWatchCommand = 'zipwatch'
        self.QbMirrorCommand = 'qbmirror'
        self.QbUnzipMirrorCommand = 'qbunpack'
        self.QbTarMirrorCommand = 'qbtarmirror'
        self.QbZipMirrorCommand = 'qbzipmirror'
        self.DeleteCommand = 'del'
        self.ShellCommand = 'shell'
        self.ExecHelpCommand = 'exechelp'
        self.TsHelpCommand = 'tshelp'

BotCommands = _BotCommands()
