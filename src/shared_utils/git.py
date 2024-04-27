import subprocess


def latest_tag():
    """
    Fetches the latest Git tag of the current project.

    Returns:
        str or None: The latest Git tag if found, None otherwise.
    """
    try:
        return (
            subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"])
            .decode()
            .strip()
        )

    except subprocess.CalledProcessError:
        return "v0.0.0"


if __name__ == "__main__":
    print(latest_tag())
