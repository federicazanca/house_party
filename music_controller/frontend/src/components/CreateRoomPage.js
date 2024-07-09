import React, { Component } from 'react';
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import {Link} from 'react-router-dom';
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import { FormLabel } from '@material-ui/core';


//We use react state to keep track of the state of the system and send info to backend
// state gets updated when things change (like if I change the votes to skip)
export default class CreateRoomPage extends Component {
    defaultVotes=2;
    constructor(props) {
        super(props);
        this.state = {
            guestCanPause: true,
            votesToSkip: this.defaultVotes,
        };
        this.handleRoomButtonPressed = this.handleRoomButtonPressed.bind(this);
        this.handleVotesChange = this.handleVotesChange.bind(this);
        this.handleGuestCanPauseChange= this.handleGuestCanPauseChange.bind(this);
    }
// gets the object that called the function (e, should be the textfield) and gets the value from there and puts it in the state
    handleVotesChange(e) {
        this.setState({
            votesToSkip: e.target.value,
        });
    }
// same but with inline if statement (ternary if) since this takes boolean
    handleGuestCanPauseChange(e) {
        this.setState({
            guestCanPause: e.target.value === 'true' ? true : false,
        })
    }
// event for when you press the create room button
// send request to api create room, once we get a response let's convert it intop json and print it
    handleRoomButtonPressed() {
        const requestOptions = {
            method: 'POST',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify({
                votes_to_skip: this.state.votesToSkip,
                guest_can_pause: this.state.guestCanPause
            }),
        };
        fetch('/api/create-room', requestOptions).then((response)=>
        response.json()
        ).then((data)=>console.log(data));
    }
// Here we are styiling the create page
// adding headre, small text, and buttons
// spacing 1 vuol dire 8 pixel
// xs 12 fa la grid piu larga possibile
// Typography is a nice style header
    render() {
        return (
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography component='h4' variant='h4'>
                        Create a Room
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl component='fieldset'>
                        <FormHelperText component="div">
                            <div align="center">
                                Guest Control of Playback State
                            </div>
                        </FormHelperText>
                        <RadioGroup row
                        defaultValue='true'
                        onChange={this.handleGuestCanPauseChange}>
                            <FormControlLabel
                            value="true"
                            control={<Radio color="primary"/>}
                            label="Play/Pause"
                            labelPlacement="bottom"
                            />
                            <FormControlLabel
                            value="false"
                            control={<Radio color="secondary"/>}
                            label="No control"
                            labelPlacement="bottom"
                            />
                        </RadioGroup>
                    </FormControl>
                </Grid>
                    <Grid item xs={12} align="center">
                        <FormControl>
                            <TextField
                            required="true"
                            type="number"
                            onChange={this.handleVotesChange}
                            defaultValue={this.defaultVotes}
                            inputProps = {{
                                min:1,
                                style: {textAlign: "center"}
                            }}
                            />
                            <FormHelperText>
                                <div align="center">
                                    Votes required to Skip Song
                                </div>
                            </FormHelperText>
                        </FormControl>
                        <Grid item xs={12} align="center">
                            <Button color="primary"
                            variant="contained"
                            onClick={this.handleRoomButtonPressed}>
                                Create a Room
                            </Button>
                        </Grid>
                        <Grid item xs={12} align="center">
                            <Button color="secondary" variant="contained" to="/" component={Link}>
                                Back
                            </Button>
                        </Grid>
                    </Grid>
            </Grid>
        );

    }
}
