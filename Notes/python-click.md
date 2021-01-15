> https://foofish.net/python-click.html

简单,但并不如argparse灵活,可以接受

```py
class CustomMultiCommand(click.Group):
    def command(self, *args, **kwargs):
        """Behaves the same as `click.Group.command()` except if passed
        a list of names, all after the first will be aliases for the first.
        """
        log.debug(args)
        log.debug(kwargs)

        def decorator(f):
            names = kwargs.setdefault("name")

            if names is not None and isinstance(names, list) and len(names) > 0:
                del kwargs["name"]
                for alias in names:
                    cmd = super(CustomMultiCommand, self).command(
                        *args, name=alias, **kwargs
                    )(f)
                    cmd.short_help = "Alias for '{}'".format(names[0])
            else:

                cmd = super(CustomMultiCommand, self).command(*args, **kwargs)(f)
            return cmd

        return decorator


@click.group(cls=CustomMultiCommand)
def main():
    pass


@main.command(name=["list", "l"])
def listt():
    click.echo("listt")

```