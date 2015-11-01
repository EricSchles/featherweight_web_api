import featherweight_api


def myfn(x, c):
    """Example function"""
    result = x*x + c
    return result


# If called with arguments:
# http://localhost:5000/myfn?x=2&c=10
# we get a correct output:
# {"success": true, "result": 14.0, "error_msg": null}

# If called without arguments using:
# http://localhost:5000/myfn
# then we get a useful error message
# {"result": null, "error_msg": "TypeError(\"myfn() missing 2 required positional arguments: 'x' and 'c'\",)", "success": false}

if __name__ == "__main__":
    featherweight_api.register(myfn)
    featherweight_api.run()
