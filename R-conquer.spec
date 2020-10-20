#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-conquer
Version  : 1.0.2
Release  : 3
URL      : https://cran.r-project.org/src/contrib/conquer_1.0.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/conquer_1.0.2.tar.gz
Summary  : Convolution-Type Smoothed Quantile Regression
Group    : Development/Tools
License  : GPL-3.0
Requires: R-conquer-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppArmadillo
Requires: R-matrixStats
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : R-matrixStats
BuildRequires : buildreq-R

%description
# conquer
**Con**volution-type smoothed **qu**antil**e** **r**egression
## Description

%package lib
Summary: lib components for the R-conquer package.
Group: Libraries

%description lib
lib components for the R-conquer package.


%prep
%setup -q -c -n conquer
cd %{_builddir}/conquer

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598639425

%install
export SOURCE_DATE_EPOCH=1598639425
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library conquer
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library conquer
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library conquer
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc conquer || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/conquer/DESCRIPTION
/usr/lib64/R/library/conquer/INDEX
/usr/lib64/R/library/conquer/Meta/Rd.rds
/usr/lib64/R/library/conquer/Meta/features.rds
/usr/lib64/R/library/conquer/Meta/hsearch.rds
/usr/lib64/R/library/conquer/Meta/links.rds
/usr/lib64/R/library/conquer/Meta/nsInfo.rds
/usr/lib64/R/library/conquer/Meta/package.rds
/usr/lib64/R/library/conquer/NAMESPACE
/usr/lib64/R/library/conquer/R/conquer
/usr/lib64/R/library/conquer/R/conquer.rdb
/usr/lib64/R/library/conquer/R/conquer.rdx
/usr/lib64/R/library/conquer/help/AnIndex
/usr/lib64/R/library/conquer/help/aliases.rds
/usr/lib64/R/library/conquer/help/conquer.rdb
/usr/lib64/R/library/conquer/help/conquer.rdx
/usr/lib64/R/library/conquer/help/paths.rds
/usr/lib64/R/library/conquer/html/00Index.html
/usr/lib64/R/library/conquer/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/conquer/libs/conquer.so
