import {useCallback, useEffect, useMemo, useState} from "react";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import { TableFooter, TableRow } from "@mui/material";


const makeApiCall = async (offset = 0, limit = 10) => {
    const apiUrl = `https://api.opendota.com/api/explorer?sql=select%20*%20from%20matches%20order%20by%20start_time%20desc%20limit%20${limit}%20offset%20${offset}`;
    const url = apiUrl;
    const res = await fetch(url);
    return res.json();
}
const cols = ['match_id', 'start_time', 'duration', 'first_blood_time', 'radiant_score', 'dire_score'];
const TeamTable = ({rows = [], pagination}) => {
    const { count, page, rowsPerPage, onPageChange, onRowsPerPageChange } = pagination;
    const tColHeadings = (
        <TableRow>
            {cols.map(col => <TableCell>{col}</TableCell>)}
        </TableRow>
    );
    const tRows = rows.map(row => (
        <TableRow>{cols.map(col => <TableCell>{row[col]}</TableCell>)}</TableRow>
    ));

    return (
        <> {pagination &&
            <TableContainer sx={{maxHeight: 440}}>
                <Table>
                    <TableHead>
                        {tColHeadings}
                    </TableHead>
                    <TableBody>
                        {tRows}
                    </TableBody>
                    <TableFooter>
                        <TableRow>
                            <TablePagination
                                rowsPerPageOptions={[5, 10, 25, { label: 'All', value: -1 }]}
                                colSpan={3}
                                count={count}
                                rowsPerPage={rowsPerPage}
                                page={page}
                                SelectProps={{
                                    inputProps: {
                                    'aria-label': 'rows per page',
                                    },
                                    native: true,
                                }}
                                onPageChange={onPageChange}
                                onRowsPerPageChange={onRowsPerPageChange}>
                            </TablePagination>
                        </TableRow>
                    </TableFooter>
                </Table>
            </TableContainer>
            }
        </>
    );
};
export const TableController = () => {
    const [rows, setRows] = useState([]);
    const [rowsPerPage, setRowsPerPage] = useState(10);
    const [page, setPage] = useState(0);
    const getTableData = useCallback(
      (page, rowsPerPage) => {
        makeApiCall(page*rowsPerPage, rowsPerPage).then(res => {
            if (res && res.rows) {
                setRows(res.rows);
                setPage(page);
                setRowsPerPage(rowsPerPage);
            }
        }).catch(err => {
            console.log(err);
        });
      },
      [],
    );

    useEffect(() => {
        getTableData(page, rowsPerPage);
    }, [getTableData]);

    const onPageChange = useCallback((event, newPage) => {
        getTableData(newPage, rowsPerPage);
    }, []);

    const onRowsPerPageChange = useCallback((event) => {
        getTableData(page, +event.target.value);
    }, []);

    const paginationProps = useMemo(() => {
        return {
            count: 1000,
            page: page,
            rowsPerPage: rowsPerPage,
            onPageChange: onPageChange,
            onRowsPerPageChange: onRowsPerPageChange
        };
    }, [rows, page, rowsPerPage]);
    return (
        <>
            <TeamTable rows = {rows || []} pagination={paginationProps} />
        </>
    );
};

