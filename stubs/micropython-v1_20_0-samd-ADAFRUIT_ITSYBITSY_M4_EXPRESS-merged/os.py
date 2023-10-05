"""
Basic "operating system" services.

MicroPython module: https://docs.micropython.org/en/v1.20.0/library/os.html

CPython module: :mod:`python:os` https://docs.python.org/3/library/os.html .

The ``os`` module contains functions for filesystem access and mounting,
terminal redirection and duplication, and the ``uname`` and ``urandom``
functions.
"""
# MCU: OrderedDict({'build': '', 'ver': 'v1.20.0', 'version': '1.20.0', 'port': 'samd', 'board': 'ADAFRUIT_ITSYBITSY_M4_EXPRESS', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51G19A', 'arch': 'armv7emsp'})
# Stubber: v1.13.7
from typing import IO, Iterator, Optional, Tuple, Any
from _typeshed import Incomplete
from stdlib.os import *


def rmdir(path) -> None:
    """
    Remove a directory.
    """
    ...


def rename(old_path, new_path) -> None:
    """
    Rename a file.
    """
    ...


def mount(fsobj, mount_point, *, readonly=False) -> Incomplete:
    """
    Mount the filesystem object *fsobj* at the location in the VFS given by the
    *mount_point* string.  *fsobj* can be a a VFS object that has a ``mount()``
    method, or a block device.  If it's a block device then the filesystem type
    is automatically detected (an exception is raised if no filesystem was
    recognised).  *mount_point* may be ``'/'`` to mount *fsobj* at the root,
    or ``'/<name>'`` to mount it at a subdirectory under the root.

    If *readonly* is ``True`` then the filesystem is mounted read-only.

    During the mount process the method ``mount()`` is called on the filesystem
    object.

    Will raise ``OSError(EPERM)`` if *mount_point* is already mounted.
    """
    ...


def mkdir(path) -> Incomplete:
    """
    Create a new directory.
    """
    ...


def urandom(n) -> bytes:
    """
    Return a bytes object with *n* random bytes. Whenever possible, it is
    generated by the hardware random number generator.
    """
    ...


def stat(path) -> Incomplete:
    """
    Get the status of a file or directory.
    """
    ...


def unlink(*args, **kwargs) -> Any:
    ...


def umount(mount_point) -> Incomplete:
    """
    Unmount a filesystem. *mount_point* can be a string naming the mount location,
    or a previously-mounted filesystem object.  During the unmount process the
    method ``umount()`` is called on the filesystem object.

    Will raise ``OSError(EINVAL)`` if *mount_point* is not found.
    """
    ...


def statvfs(path) -> Tuple:
    """
    Get the status of a fileystem.

    Returns a tuple with the filesystem information in the following order:

         * ``f_bsize`` -- file system block size
         * ``f_frsize`` -- fragment size
         * ``f_blocks`` -- size of fs in f_frsize units
         * ``f_bfree`` -- number of free blocks
         * ``f_bavail`` -- number of free blocks for unprivileged users
         * ``f_files`` -- number of inodes
         * ``f_ffree`` -- number of free inodes
         * ``f_favail`` -- number of free inodes for unprivileged users
         * ``f_flag`` -- mount flags
         * ``f_namemax`` -- maximum filename length

    Parameters related to inodes: ``f_files``, ``f_ffree``, ``f_avail``
    and the ``f_flags`` parameter may return ``0`` as they can be unavailable
    in a port-specific implementation.
    """
    ...


def chdir(path) -> Incomplete:
    """
    Change current directory.
    """
    ...


def listdir(dir: Optional[Any] = None) -> Incomplete:
    """
    With no argument, list the current directory.  Otherwise list the given directory.
    """
    ...


def remove(path) -> None:
    """
    Remove a file.
    """
    ...


def dupterm(stream_object, index=0, /) -> IO:
    """
    Duplicate or switch the MicroPython terminal (the REPL) on the given `stream`-like
    object. The *stream_object* argument must be a native stream object, or derive
    from ``io.IOBase`` and implement the ``readinto()`` and
    ``write()`` methods.  The stream should be in non-blocking mode and
    ``readinto()`` should return ``None`` if there is no data available for reading.

    After calling this function all terminal output is repeated on this stream,
    and any input that is available on the stream is passed on to the terminal input.

    The *index* parameter should be a non-negative integer and specifies which
    duplication slot is set.  A given port may implement more than one slot (slot 0
    will always be available) and in that case terminal input and output is
    duplicated on all the slots that are set.

    If ``None`` is passed as the *stream_object* then duplication is cancelled on
    the slot given by *index*.

    The function returns the previous stream-like object in the given slot.
    """
    ...


def ilistdir(dir: Optional[Any] = None) -> Iterator[Tuple]:
    """
    This function returns an iterator which then yields tuples corresponding to
    the entries in the directory that it is listing.  With no argument it lists the
    current directory, otherwise it lists the directory given by *dir*.

    The tuples have the form *(name, type, inode[, size])*:

     - *name* is a string (or bytes if *dir* is a bytes object) and is the name of
       the entry;
     - *type* is an integer that specifies the type of the entry, with 0x4000 for
       directories and 0x8000 for regular files;
     - *inode* is an integer corresponding to the inode of the file, and may be 0
       for filesystems that don't have such a notion.
     - Some platforms may return a 4-tuple that includes the entry's *size*.  For
       file entries, *size* is an integer representing the size of the file
       or -1 if unknown.  Its meaning is currently undefined for directory
       entries.
    """
    ...


def getcwd() -> Incomplete:
    """
    Get the current directory.
    """
    ...


class VfsLfs2:
    """
    Create a filesystem object that uses the `littlefs v2 filesystem format`_.
    Storage of the littlefs filesystem is provided by *block_dev*, which must
    support the :ref:`extended interface <block-device-interface>`.
    Objects created by this constructor can be mounted using :func:`mount`.

    The *mtime* argument enables modification timestamps for files, stored using
    littlefs attributes.  This option can be disabled or enabled differently each
    mount time and timestamps will only be added or updated if *mtime* is enabled,
    otherwise the timestamps will remain untouched.  Littlefs v2 filesystems without
    timestamps will work without reformatting and timestamps will be added
    transparently to existing files once they are opened for writing.  When *mtime*
    is enabled `os.stat` on files without timestamps will return 0 for the timestamp.

    See :ref:`filesystem` for more information.
    """

    def rename(self, *args, **kwargs) -> Any:
        ...

    @staticmethod
    def mkfs(block_dev, readsize=32, progsize=32, lookahead=32) -> None:
        """
            Build a Lfs2 filesystem on *block_dev*.

        ``Note:`` There are reports of littlefs v2 failing in certain situations,
                  for details see `littlefs issue 295`_.
        """
        ...

    def mount(self, *args, **kwargs) -> Any:
        ...

    def statvfs(self, *args, **kwargs) -> Any:
        ...

    def rmdir(self, *args, **kwargs) -> Any:
        ...

    def stat(self, *args, **kwargs) -> Any:
        ...

    def umount(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def mkdir(self, *args, **kwargs) -> Any:
        ...

    def open(self, *args, **kwargs) -> Any:
        ...

    def ilistdir(self, *args, **kwargs) -> Any:
        ...

    def chdir(self, *args, **kwargs) -> Any:
        ...

    def getcwd(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, block_dev, readsize=32, progsize=32, lookahead=32, mtime=True) -> None:
        ...


class VfsFat:
    """
    Create a filesystem object that uses the FAT filesystem format.  Storage of
    the FAT filesystem is provided by *block_dev*.
    Objects created by this constructor can be mounted using :func:`mount`.
    """

    def rename(self, *args, **kwargs) -> Any:
        ...

    @staticmethod
    def mkfs(block_dev) -> None:
        """
        Build a FAT filesystem on *block_dev*.
        """
        ...

    def mount(self, *args, **kwargs) -> Any:
        ...

    def statvfs(self, *args, **kwargs) -> Any:
        ...

    def rmdir(self, *args, **kwargs) -> Any:
        ...

    def stat(self, *args, **kwargs) -> Any:
        ...

    def umount(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def mkdir(self, *args, **kwargs) -> Any:
        ...

    def open(self, *args, **kwargs) -> Any:
        ...

    def ilistdir(self, *args, **kwargs) -> Any:
        ...

    def chdir(self, *args, **kwargs) -> Any:
        ...

    def getcwd(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, block_dev) -> None:
        ...


class VfsLfs1:
    """
    Create a filesystem object that uses the `littlefs v1 filesystem format`_.
    Storage of the littlefs filesystem is provided by *block_dev*, which must
    support the :ref:`extended interface <block-device-interface>`.
    Objects created by this constructor can be mounted using :func:`mount`.

    See :ref:`filesystem` for more information.
    """

    def rename(self, *args, **kwargs) -> Any:
        ...

    @staticmethod
    def mkfs(block_dev, readsize=32, progsize=32, lookahead=32) -> None:
        """
            Build a Lfs1 filesystem on *block_dev*.

        ``Note:`` There are reports of littlefs v1 failing in certain situations,
                  for details see `littlefs issue 347`_.
        """
        ...

    def mount(self, *args, **kwargs) -> Any:
        ...

    def statvfs(self, *args, **kwargs) -> Any:
        ...

    def rmdir(self, *args, **kwargs) -> Any:
        ...

    def stat(self, *args, **kwargs) -> Any:
        ...

    def umount(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def mkdir(self, *args, **kwargs) -> Any:
        ...

    def open(self, *args, **kwargs) -> Any:
        ...

    def ilistdir(self, *args, **kwargs) -> Any:
        ...

    def chdir(self, *args, **kwargs) -> Any:
        ...

    def getcwd(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, block_dev, readsize=32, progsize=32, lookahead=32) -> None:
        ...
