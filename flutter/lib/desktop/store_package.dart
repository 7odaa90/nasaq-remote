import 'dart:io';

/// True when running from an installed Microsoft Store (MSIX) package.
/// Such a copy is already installed and updated by the Store: installing it again
/// would copy its files out of the signed package.
bool get isStorePackage =>
    Platform.isWindows &&
    Platform.resolvedExecutable.toLowerCase().contains(r'\windowsapps\');
