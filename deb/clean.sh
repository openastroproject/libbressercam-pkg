#!/bin/bash

version=`cat version`

rm -fr libbressercam-$version
rm -fr libbressercam_*
rm -fr libbressercam-dev_*
rm -f debfiles/compat
rm -f debfiles/patches/*
