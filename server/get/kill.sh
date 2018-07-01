#!/bin/bash
ps -aux | grep get.py | awk '{print $2}' | xargs kill -9
