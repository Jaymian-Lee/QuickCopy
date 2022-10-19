<h1>QuickCopy</h1>

<h3>Demo version 1.0.0<h3>

<h2>*STILL IN PROGRESS*</h2>
 
<h3>QuickCopy CLI created for easy use of <a target="blank" href="https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy">robocopy</a> command</h3>

<p>(Currently the only options are to copy files and directories. The copy options still need to be added to the project)</p>

<p>QuickCopy makes it possible to select the desired source and destination directories or files. Its also possible to select the desired Copy options such as:</p>

  <pre>Option 	Description
/s 	Copies subdirectories. This option automatically excludes empty directories.
/e 	Copies subdirectories. This option automatically includes empty directories.
/lev:<n> 	Copies only the top n levels of the source directory tree.
/z 	Copies files in restartable mode. In restartable mode, should a file copy be interrupted, Robocopy can pick up where it left off rather than recopying the entire file.
/b 	Copies files in backup mode. Backup mode allows Robocopy to override file and folder permission settings (ACLs). This allows you to copy files you might otherwise not have access to, assuming it's being run under an account with sufficient privileges.
/zb 	Copies files in restartable mode. If file access is denied, switches to backup mode.
/j 	Copies using unbuffered I/O (recommended for large files).
/efsraw 	Copies all encrypted files in EFS RAW mode.
/copy:<copyflags> 	Specifies which file properties to copy. The valid values for this option are:

    D - Data
    A - Attributes
    T - Time stamps
    S - NTFS access control list (ACL)
    O - Owner information
    U - Auditing information

The default value for this option is DAT (data, attributes, and time stamps).
/dcopy:<copyflags> 	Specifies what to copy in directories. The valid values for this option are:

    D - Data
    A - Attributes
    T - Time stamps

The default value for this option is DA (data and attributes).
/sec 	Copies files with security (equivalent to /copy:DATS).
/copyall 	Copies all file information (equivalent to /copy:DATSOU).
/nocopy 	Copies no file information (useful with /purge).
/secfix 	Fixes file security on all files, even skipped ones.
/timfix 	Fixes file times on all files, even skipped ones.
/purge 	Deletes destination files and directories that no longer exist in the source. Using this option with the /e option and a destination directory, allows the destination directory security settings to not be overwritten.
/mir 	Mirrors a directory tree (equivalent to /e plus /purge). Using this option with the /e option and a destination directory, overwrites the destination directory security settings.
/mov 	Moves files, and deletes them from the source after they are copied.
/move 	Moves files and directories, and deletes them from the source after they are copied.
/a+:[RASHCNET] 	Adds the specified attributes to copied files. The valid values for this option are:

    R - Read only
    A - Archive
    S - System
    H - Hidden
    C - Compressed
    N - Not content indexed
    E - Encrypted
    T - Temporary

/a-:[RASHCNET] 	Removes the specified attributes from copied files. The valid values for this option are:

    R - Read only
    A - Archive
    S - System
    H - Hidden
    C - Compressed
    N - Not content indexed
    E - Encrypted
    T - Temporary

/create 	Creates a directory tree and zero-length files only.
/fat 	Creates destination files by using 8.3 character-length FAT file names only.
/256 	Turns off support for paths longer than 256 characters.
/mon:<n> 	Monitors the source, and runs again when more than n changes are detected.
/mot:<m> 	Monitors the source, and runs again in m minutes, if changes are detected.
/mt[:n] 	Creates multi-threaded copies with n threads. n must be an integer between 1 and 128. The default value for n is 8. For better performance, redirect your output using /log option.

The /mt parameter can't be used with the /ipg and /efsraw parameters.
/rh:hhmm-hhmm 	Specifies run times when new copies may be started.
/pf 	Checks run times on a per-file (not per-pass) basis.
/ipg:n 	Specifies the inter-packet gap to free bandwidth on slow lines.
/sj 	Copies junctions (soft-links) to the destination path instead of link targets.
/sl 	Don't follow symbolic links and instead create a copy of the link.
/nodcopy 	Copies no directory info (the default /dcopy:DA is done).
/nooffload 	Copies files without using the Windows Copy Offload mechanism.
/compress 	Requests network compression during file transfer, if applicable.</pre>
