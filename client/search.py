from os import path
try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk

extensions = dict(documents=[
    "pdf",
    "rtf",
    "doc",
    "dot",
    "docx",
    "docm",
    "dotm",
    "docb",
    "xls",
    "xlt",
    "xlm",
    "xlsx",
    "xlsm",
    "xltx",
    "xltm",
    "xlsb",
    "xla",
    "xlam",
    "xll",
    "xlw",
    "ppt",
    "pot",
    "ppt",
    "pps",
    "pptx"
    "pptm",
    "potx",
    "potm",
    "ppam",
    "ppsx",
    "ppsm",
    "sldx",
    "sdm",
    "mpd",
    "mpp",
    "mpt",
    "mpc",
    "mpv",
    "mxm",
    "vsd",
    "vsdx",
    "odt",
    "ott",
    "odm",
    "oth",
    "ods",
    "ots",
    "odg",
    "otg",
    "cdp",
    "otp",
    "odf",
    "oxt"
], plain_text=[
    "txt",
    "csv",
    "html"
], databases=[
    "db",
    "odb",
    "sqlite",
    "sql",
    "db3",
    "dbf",
    "sdb",
    "ibd",
    "db-journal",
    "db3",
    "dbf",
    "myd",
    "rsd",
    "sdf",
    "s3db",
    "ade",
    "adp",
    "adn",
    "accdb",
    "accdr",
    "accdt"
    "accda"
    "mdb",
    "cdb",
    "mda",
    "mda",
    "mdn",
    "mdt",
    "mdw",
    "mdf",
    "mde",
    "accde",
    "mam",
    "maq",
    "mar",
    "mat",
    "maf"
], images=[
    "jpg",
    "jpeg",
    "exif",
    "tiff",
    "gif",
    "bmp",
    "png"
    "ppm",
    "pgm",
    "pbm",
    "pnm",
    "webp",
    "bgp",
    "svg",
    "psd"
], audio=[
    "3gp",
    "act",
    "aiff",
    "acc",
    "ape",
    "au",
    "awb",
    "dct",
    "dvf",
    "flac",
    "gsm",
    "iklax",
    "ivs",
    "m4a",
    "m4p",
    "mp3",
    "mpc",
    "mpc",
    "msv",
    "ogg",
    "oga",
    "opus",
    "ra",
    "rm",
    "sln",
    "vox",
    "wav",
    "wma",
    "wv"
], video=[
    "webm",
    "flv",
    "vob",
    "ogv",
    "ogg",
    "drc",
    "gifv",
    "mng",
    "avi",
    "mov",
    "qt",
    "wmv",
    "rm",
    "rmvb",
    "asf",
    "mp4",
    "m4p",
    "m4v",
    "mpg",
    "mp2",
    "mpeg",
    "mpe",
    "mpv",
    "mpg",
    "mpeg",
    "m2v",
    "m4v",
    "svi",
    "3gp",
    "mxf",
    "nsv",
    "f4v",
    "f4p",
    "f4a",
    "f4b"
], archives=[
    "zip",
    "rar",
    "ace",
    "7z",
    "tar"
    "gz",
    "bz2",
    "iso",
    "dmg"
],emails=[
    "msg",
    "eml",
    "pst"
], p2p=[
    "torrent"
], pki=[
    "key",
    "csr",
    "pem",
    "p7b"
], exes=[
    "exe",
    "com",
    "msi",
    "bat",
    "ps1",
    "sh",
    "pkg"
], cad=[
    "hpgl",
    "igs",
    "step",
    "stp",
    "fas",

], source=[
    "h",
    "c",
    "cpp"
    "java",
    "asp",
    "aspx",
    "vcproj",
    "vbw",
    "cs",
    "fs",
    "bat",
    "vbs",
    "csx",
    "ps1",
    "cgi",
    "lua",
    "pl",
    "pm",
    "prl",
    "py",
    "axd",
    "php",
    "php3",
    "json",
    "do",
    "js",
    "css",
    "html",
    "asm",
    "asi",
    "sh"
]
)

all_extensions = []

for ext_type in extensions:
    all_extensions += extensions[ext_type]

all_extensions = set(all_extensions)


def get_extentions_by_type(ext_types):
    selected_extensions = []
    for ext_type in ext_types:
        selected_extensions += extensions[ext_type]
    return set(selected_extensions)


def find_files(root_path, filter_extensions=all_extensions):
    paths = []
    for root, dirs, files in walk(root_path):
            for file in files:
                filename_parts = file.split(".")
                if len(filename_parts) < 2 or file.startswith("~$"):
                    continue
                file_extension = filename_parts[-1]
                if file_extension.lower() in filter_extensions:
                    paths.append(path.join(root, file))
    return paths


def get_recent_files(paths, n=None):
    paths = sorted(paths, key=path.getmtime, reverse=True)
    if n:
        paths = paths[:n]
    return paths


def basename_paths(paths):
    return map(lambda x: path.basename(x), paths)

