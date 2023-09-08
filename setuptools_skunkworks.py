"""Example setuptools plugin that just loggs its calls."""

import typing

from setuptools import Command, Distribution


# pylint: disable-next=invalid-name
class build_skunkworks(Command):
    """Example build command."""

    def __init__(self, dist: Distribution, **kwargs: typing.Any) -> None:
        """Create and initialize a new Command object."""
        self.build_lib = None
        super().__init__(dist, **kwargs)

    def initialize_options(self) -> None:
        """Set default values for all the options that this command supports."""
        print("SKUNKWORKS: build_skunkworks.initialize_options() called.")
        self.build_lib = None

    def finalize_options(self) -> None:
        """Set final values for all the options that this command supports."""
        print("SKUNKWORKS: build_skunkworks.finalize_options() called.")
        self.set_undefined_options("build", ("build_lib", "build_lib"))

    def run(self) -> None:
        """Command's raison d'etre: carry out the action it exists to perform."""
        print("SKUNKWORKS: build_skunkworks.run() called.")
        print(f"SKUNKWORKS: build_lib = {self.build_lib!r}")


# pylint: disable-next=invalid-name
class clean_skunkworks(Command):
    """Example clean command."""

    def initialize_options(self) -> None:
        """Set default values for all the options that this command supports."""
        print("SKUNKWORKS: clean_skunkworks.initialize_options() called.")

    def finalize_options(self) -> None:
        """Set final values for all the options that this command supports."""
        print("SKUNKWORKS: clean_skunkworks.finalize_options() called.")

    def run(self) -> None:
        """Command's raison d'etre: carry out the action it exists to perform."""
        print("SKUNKWORKS: clean_skunkworks.run() called.")


# pylint: disable-next=invalid-name
class install_skunkworks(Command):
    """Example install command."""

    def initialize_options(self) -> None:
        """Set default values for all the options that this command supports."""
        print("SKUNKWORKS: install_skunkworks.initialize_options() called.")

    def finalize_options(self) -> None:
        """Set final values for all the options that this command supports."""
        print("SKUNKWORKS: install_skunkworks.finalize_options() called.")

    def run(self) -> None:
        """Command's raison d'etre: carry out the action it exists to perform."""
        print("SKUNKWORKS: install_skunkworks.run() called.")


def has_skunkworks(command: Command) -> bool:
    """Check if the project enables skunkworks."""
    print(f"SKUNKWORKS: has_skunkworks_units({command!r}) called.***")
    return True


def finalize_distribution_options(dist: Distribution) -> None:
    """Plug the extension into setuptools."""
    print(f"SKUNKWORKS: finalize_distribution_options({dist!r}) called.")
    build = dist.get_command_class("build")
    print(f"SKUNKWORKS: Appending build_skunkworks to {build} sub-commands...")
    build.sub_commands.append(("build_skunkworks", has_skunkworks))
    print(f"SKUNKWORKS: build.sub_commands = {build.sub_commands!r}")

    # Note: setuptools has no clean sub-commands!
    clean = dist.get_command_class("clean")
    print(f"SKUNKWORKS: Appending clean_skunkworks to {clean} sub-commands...")
    clean.sub_commands.append(("clean_skunkworks", has_skunkworks))
    print(f"SKUNKWORKS: clean.sub_commands = {clean.sub_commands!r}")

    install = dist.get_command_class("install")
    print(f"SKUNKWORKS: Appending install_skunkworks to {install} sub-commands...")
    install.sub_commands.append(("install_skunkworks", has_skunkworks))
    print(f"SKUNKWORKS: install.sub_commands = {install.sub_commands!r}")
